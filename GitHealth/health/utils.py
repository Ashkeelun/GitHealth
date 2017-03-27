import requests
import re


def get_dir_re(domain):
    # print(domain)
    platform_dir_re_dict = {
        'https://github.com': re.compile(r'<a.*?href="(.+?)".*?class="js-navigation-open".*?>(?:<span.*?<\/span>)?(.+?)(\..*)?<\/a>'),
    }
    return platform_dir_re_dict[domain]


def rm_html_escapes(html):
    html_escapes = [('&#39;', "'"), ('&quot;', '"'), ('&gt;', '>'), ('&lt;', '<'), ('&amp;', '&')]
    for escape in html_escapes:
        html = html.replace(escape[0], escape[1])
    return html

class Repo:
    name = 'name'

    def __init__(self, url):
        self.url = url
        # print(url)
        url_parts = re.findall(re.compile(r'((?:https?:\/\/).*?)(\/.*)?$'), url)
        # print(url_parts)
        self.url_path = url_parts[0][1]
        self.domain = url_parts[0][0]
        self.dir_re = get_dir_re(self.domain)
        # req = requests.get(self.url).text
        self.dir =Dir(self, self.url_path, "repo name")

    def __str__(self):
        pass


class File:

    def __init__(self, dir, url, name, type):
        self.dir = dir
        # self.dir_re = get_dir_re(self.repo.domain)
        self.url = url
        self.name = name
        self.type = type
        # use domain for file reading: https://raw.githubusercontent.com
        file_page = requests.get(self.dir.repo.domain + self.url).text
        raw_line_re = re.compile(r'<td.*?class=".*?js-file-line.*?".*?>(.*?)<\/td>')
        raw_lines = '\n'.join(re.findall(raw_line_re, file_page))
        rm_span_re = re.compile(r'(?:<span.*?>|<\/span>)')
        lines = rm_html_escapes(re.sub(rm_span_re, '', raw_lines))

        slc_re = re.compile(r'#.*')
        mlc_re = re.compile(r'["\']{3}((?:.|\n)*?)["\']{3}')
        alc_re = re.compile(r'(?:["\']{3}((?:.|\n)*?)["\']{3}|#.*)')
        slcs = re.findall(slc_re, lines)
        mlcs = re.findall(mlc_re, lines)
        code = re.sub(alc_re, '', lines)
        self.comt_size = len(''.join(slcs) + ''.join(mlcs))
        self.code_size = len(code)
        self.slc_num = len(slcs)
        self.mlc_num = len(mlcs)
        self.slc_size = len(''.join(slcs))
        self.mlc_size = len(''.join(mlcs))
        print("----- {}{} -----\nCode Size: {}\nComment Size: {}".format(self.name, self.type, self.code_size, self.comt_size))



class Dir:

    def __init__(self, repo, url, name, parent=None):
        self.repo = repo
        self.dir_re = get_dir_re(self.repo.domain)
        self.url = url
        self.name = name
        self.parent = parent
        self.sub_dirs = []
        self.sub_files = []
        req = requests.get(self.repo.domain + self.url).text
        contents = re.findall(self.dir_re, req)
        for content in contents:
            if content[2] == '.py':
                print(content[1] + "  " + content[2] + " - " + content[0])
                self.sub_dirs.append(File(self, content[0], content[1], content[2]))
            elif not content[2]:
                print(content[1] + "  " + content[2] + " - " + content[0])
                self.sub_dirs.append(Dir(self.repo, content[0], content[1], self))


