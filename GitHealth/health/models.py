from django.db import models
from django.core.urlresolvers import reverse
import requests
from time import sleep

from .utils import *


# Repository Table

class RepositoryManager(models.Manager):
    def create_repository(self, url):
        repo = requests.get(url).text
        domain = get_url_parts(url)[0]
        name = re.findall(get_repo_name_re(domain), repo)[0]
        last_commit = re.findall(get_commit_re(domain), repo)[0]
        root = Directory.manage.create_directory(domain=domain, path=get_url_parts(url)[1], name=name)
        return self.create(name=name, url=url, last_commit=last_commit, root=root)


class Repository(models.Model):
    name = models.CharField(max_length=150,)
    url = models.URLField(max_length=250,)
    last_commit = models.CharField(max_length=150)
    root = models.ForeignKey('Directory', on_delete=models.CASCADE, blank=True, null=True, related_name="repository",)

    manage = RepositoryManager()
    objects = models.Manager()

    def __str__(self):
        return self.name + ': ' + self.url

    def get_domain(self):
        return get_url_parts(self.url)[0]

    def get_path(self):
        return get_url_parts(self.url)[1]

    def document_stats(self):
        return self.root.total_doc_info()


# Directory Table

class DirectoryManager(models.Manager):
    def create_directory(self, domain, path, name, parent=None):
        url = domain+path
        dir_html = requests.get(url).text
        last_commit = re.findall(get_commit_re(domain), dir_html)[0]
        if parent:
            dir = self.create(name=name, url=url, last_commit=last_commit, parent_dir=parent)
        else:
            dir = self.create(name=name, url=url, last_commit=last_commit)
        contents = re.findall(get_dir_re(domain), dir_html)
        for content in contents:
            if not content[3] and content[0] == "file-directory":
                Directory.manage.create_directory(domain=domain, path=content[1], name=content[2], parent=dir)
            elif is_file_sup(content[3]):
                File.manage.create_file(domain=domain, path=content[1], name=content[2], extension=content[3], parent=dir)
            # sleep(1)
        return dir


class Directory(models.Model):
    name = models.CharField(max_length=100,)
    url = models.URLField(max_length=250,)
    last_commit = models.CharField(max_length=150)
    parent_dir = models.ForeignKey('Directory', on_delete=models.CASCADE, blank=True, null=True, related_name="sub_dirs",)

    manage = DirectoryManager()
    objects = models.Manager()

    def __str__(self):
        return self.name + ': ' + self.url

    def get_domain(self):
        return get_url_parts(self.url)[0]

    def get_path(self):
        return get_url_parts(self.url)[1]

    def total_doc_info(self):
        resaults = {}
        for file_info in self.gen_doc_info():
            for key, value in file_info.items():
                try:
                    resaults[key] += value
                except KeyError:
                    resaults[key] = value
        return resaults

    def gen_doc_info(self):
        files = []
        for file in self.sub_files.all():
            files.append(file.gen_doc_info())
        for dir in self.sub_dirs.all():
            files += dir.gen_doc_info()
        return files


# File Table

class FileManager(models.Manager):
    def create_file(self, domain, path, name, extension, parent):
        # raw_domain = 'https://raw.githubusercontent.com' # use domain for raw file reading: https://raw.githubusercontent.com
        url = domain+path
        file_html = requests.get(url).text
        lines = get_lines(domain, file_html)
        slcs = re.findall(get_slc_re(extension), lines)
        mlcs = re.findall(get_mlc_re(extension), lines)
        code = re.sub(get_alc_re(extension), '', lines)
        return self.create(name=name, extension=extension, url=url, parent_dir=parent,
                           mlc_size=len(''.join(mlcs)), mlc_num=len(mlcs), slc_size=len(''.join(slcs)), slc_num=len(slcs),
                           comt_size=len(''.join(slcs) + ''.join(mlcs)), code_size=len(code))


class File(models.Model):
    name = models.CharField(max_length=200,)
    extension = models.CharField(max_length=15,)
    url = models.URLField(max_length=250,)
    parent_dir = models.ForeignKey(Directory, on_delete=models.CASCADE, blank=True, null=True, related_name="sub_files",)
    mlc_size = models.IntegerField()
    mlc_num = models.IntegerField()
    slc_size = models.IntegerField()
    slc_num = models.IntegerField()
    comt_size = models.IntegerField()
    code_size = models.IntegerField()

    manage = FileManager()
    objects = models.Manager()

    def __str__(self):
        return self.name + ': ' + self.url

    def get_domain(self):
        return get_url_parts(self.url)[0]

    def get_path(self):
        return get_url_parts(self.url)[1]

    def gen_doc_info(self):
        return {'mlcNum': self.mlc_num, 'mlcSize': self.mlc_size,
                'slcNum': self.slc_num, 'slcSize': self.slc_size,
                'comtSize': self.comt_size, 'codeSize': self.code_size}
