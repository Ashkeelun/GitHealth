from utils import *


def rm_html_escapes(html):
    html_escapes = [('&#39;', "'"), ('&quot;', '"'), ('&gt;', '>'), ('&lt;', '<'), ('&amp;', '&')]
    for escape in html_escapes:
        html = html.replace(escape[0], escape[1])
    return html


def get_file(ref, name, ext):
    file_page = requests.get("https://github.com" + ref).text
    raw_line_re = re.compile(r'<td.*?class=".*?js-file-line.*?".*?>(.*?)<\/td>')
    raw_lines = '\n'.join(re.findall(raw_line_re, file_page))
    rm_span_re = re.compile(r'(?:<span.*?>|<\/span>)')
    lines = rm_html_escapes(re.sub(rm_span_re,'',raw_lines))
    # print('\nFile Name: '+name+ext+'\n----------------------------------------\n\n'+lines+'\n\n')
    return (name, ext, lines,)


def parse_file_str(lines):
    slc_re = re.compile(r'#.*')
    mlc_re = re.compile(r'["\']{3}((?:.|\n)*?)["\']{3}')
    alc_re = re.compile(r'(?:["\']{3}((?:.|\n)*?)["\']{3}|#.*)')
    slcs = re.findall(slc_re, lines)
    mlcs = re.findall(mlc_re, lines)
    code = re.sub(alc_re, '', lines)
    comt_len = len(''.join(slcs)+''.join(mlcs))
    code_len = len(code)
    # print("\n\nMetrics: {}, {}, {}, {}, {}, {}\n\n".format(len(slcs), len(mlcs), len(''.join(slcs)), len(''.join(mlcs)), comt_len, code_len))
    meta = [len(slcs), len(mlcs), len(''.join(slcs)), len(''.join(mlcs)), comt_len, code_len]
    return meta


req = requests.get("https://github.com/OSSHealth/ghdata/tree/dev")
r = req.text
dir_re = re.compile(r'<a.*?href="(.+?)".*?class="js-navigation-open".*?>(?:<span.*?<\/span>)?(.+?)(\..*)?<\/a>')
dirs = re.findall(dir_re, r)
metrics = []



for dir in dirs:
    print(dir[1] + "  " + dir[2] + " - " + dir[0])
    if dir[2] == '.py':
        f = get_file(dir[0], dir[1], dir[2])
        m = parse_file_str(f[2])
        metrics.append({'name': dir[1],
                        'ext': dir[2],
                        'url': dir[0],
                        'number of line Comments': m[0],
                        'number of multi-line Comments': m[1],
                        'size of line comments': m[2],
                        'size of multi-line Comments': m[3],
                        'size of Comments': m[4],
                        'size of Code': m[5]
                        })
print("\n")
for file in metrics:
    for m in file:
        print("{}: {}".format(m, file[m]))
    print("\n")




repo = Repo(r'https://github.com/OSSHealth/ghdata/tree/dev')
# print(repo.dir.name)


# for file in repo.dir.sub_files:
#     for m in file:
#         print("{}: {}".format(file.name, file.comt_size))
#     print("\n")