import re


def get_url_parts(url):
    return re.findall(re.compile(r'((?:https?:\/\/).*?)(\/.*)?$'), url)[0]


def get_repo_name_re(domain):
    platform_dict = {
        'https://github.com': re.compile(r'<title>.*\/(.*?)<\/title>'),
    }
    return platform_dict[domain]


def get_commit_re(domain):
    platform_dict = {
        'https://github.com': re.compile(r'<.*?class=".*?commit-tease.*?".*?(?:src|href)=".*?\/(?:tree-)?commit\/(\w*?)(?:\/.*?)?".*?>'),
    }
    return platform_dict[domain]


def get_dir_re(domain):
    platform_dict = {
        'https://github.com': re.compile(r'<tr.*?class="js-navigation-item".*?>(?:.|\n)*?class="octicon octicon-(.*?)?"(?:.|\n)*?<a.*?href="(.+?)".*?class="js-navigation-open".*?>(?:<span.*?<\/span>)?(.+?)(\..*)?<\/a>'),
    }
    return platform_dict[domain]


def get_line_re(domain):
    platform_dict = {
        'https://github.com': re.compile(r'<td.*?class=".*?js-file-line.*?".*?>(.*?)<\/td>'),
    }
    return platform_dict[domain]


# -------------------------- File Functions ----------------------------


def is_file_sup(extention):
    supported_file_types = [
        '.py'
    ]
    return (extention in supported_file_types)


def get_lines(domain, file_html):
    raw_lines = '\n'.join(re.findall(get_line_re(domain), file_html))
    return rm_html_escapes(re.sub(re.compile(r'(?:<span.*?>|<\/span>)'), '', raw_lines))


def get_slc_re(extention):
    platform_dir_re_dict = {
        '.py': re.compile(r'#.*'),
    }
    return platform_dir_re_dict[extention]


def get_mlc_re(extention):
    platform_dir_re_dict = {
        '.py': re.compile(r'["\']{3}((?:.|\n)*?)["\']{3}'),
    }
    return platform_dir_re_dict[extention]


def get_alc_re(extention):
    platform_dir_re_dict = {
        '.py': re.compile(r'(?:["\']{3}((?:.|\n)*?)["\']{3}|#.*)'),
    }
    return platform_dir_re_dict[extention]


def rm_html_escapes(html):
    html_escapes = [('&#39;', "'"), ('&quot;', '"'), ('&gt;', '>'), ('&lt;', '<'), ('&amp;', '&')]
    for escape in html_escapes:
        html = html.replace(escape[0], escape[1])
    return html


# ------------------------- OLD --------------------------------
# import requests


# class Repo:
#     name = 'name'
#
#     def __init__(self, url):
#         self.url = url
#         url_parts = get_url_parts(url)
#         self.url_path = url_parts[0][1]
#         self.domain = url_parts[0][0]
#
#         self.dir = Dir(self, self.url_path, "repo name")
#
#         repository = requests.get(self.url).text
#
#     def __str__(self):
#         pass
#
#
#
# class File:
#     comt_size = 0
#     code_size = 0
#     slc_num = 0
#     mlc_num = 0
#     slc_size = 0
#     mlc_size = 0
#
#     def __init__(self, dir, url, name, type):
#         self.dir = dir
#         # self.dir_re = get_dir_re(self.repo.domain)
#         self.url = url
#         self.name = name
#         self.type = type
#         # use domain for file reading: https://raw.githubusercontent.com
#         file_page = requests.get(self.dir.repo.domain + self.url).text
#         raw_line_re = re.compile(r'<td.*?class=".*?js-file-line.*?".*?>(.*?)<\/td>')
#         raw_lines = '\n'.join(re.findall(raw_line_re, file_page))
#         rm_span_re = re.compile(r'(?:<span.*?>|<\/span>)')
#         lines = rm_html_escapes(re.sub(rm_span_re, '', raw_lines))
#
#         slcs = re.findall(get_slc_re(self.type), lines)
#         mlcs = re.findall(get_mlc_re(self.type), lines)
#         code = re.sub(get_alc_re(self.type), '', lines)
#         self.comt_size = len(''.join(slcs) + ''.join(mlcs))
#         self.code_size = len(code)
#         self.slc_num = len(slcs)
#         self.mlc_num = len(mlcs)
#         self.slc_size = len(''.join(slcs))
#         self.mlc_size = len(''.join(mlcs))
#         # print("----- {}{} -----\nCode Size: {}\nComment Size: {}".format(self.name, self.type, self.code_size, self.comt_size))
#
#     def __str__(self):
#         return "----- {}{} -----\nCode Size: {}\nComment Size: {}\n".format(self.name, self.type, self.code_size, self.comt_size)
#
#     def get_doc_info(self):
#         return {'mlcNum': self.mlc_num, 'mlcSize': self.mlc_size, 'slcNum': self.slc_num,'slcSize': self.slc_size, 'comtSize': self.comt_size, 'codeSize': self.code_size}
#
#
#
# class Dir:
#
#     def __init__(self, repo, url, name, parent=None):
#         self.repo = repo
#         self.dir_re = get_dir_re(self.repo.domain)
#         self.url = url
#         self.name = name
#         self.parent = parent
#         self.sub_dirs = []
#         self.sub_files = []
#         req = requests.get(self.repo.domain + self.url).text
#         contents = re.findall(self.dir_re, req)
#         for content in contents:
#             if content[2] == '.py':
#                 # print(content[1] + "  " + content[2] + " - " + content[0])
#                 self.sub_files.append(File(self, content[0], content[1], content[2]))
#             elif not content[2]:
#                 # print(content[1] + "  " + content[2] + " - " + content[0])
#                 self.sub_dirs.append(Dir(self.repo, content[0], content[1], self))
#
#     def __str__(self):
#         x = ''
#         for dir in self.sub_dirs:
#             x += dir.name + '\n'
#         for file in self.sub_files:
#             x = x + str(file)
#         return x
#
#     def get_doc_info(self):
#         files = []
#         for file in self.sub_files:
#             x = file.get_doc_info()
#             y = files.append(x)
#         for dir in self.sub_dirs:
#             files += dir.get_doc_info()
#         return files
#
#     def total_doc_info(self):
#         resaults = {}
#         for f in self.get_doc_info():
#             for k, v in f.items():
#                 try:
#                     resaults[k] += v
#                 except KeyError:
#                     resaults[k] = v
#         return resaults

