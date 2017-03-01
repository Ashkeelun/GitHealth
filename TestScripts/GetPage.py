import base64
import urllib
import os
import re

from github import Github

def parse_file_str(lines):
    slc_re = re.compile(r'#.*')
    mlc_re = re.compile(r"'''((?:.|\n)*?)'''")
    alc_re = re.compile(r"(?:'''(?:.|\n)*?'''|#.*)")
    
    slcs = re.findall(slc_re, lines)
    mlcs = re.findall(mlc_re, lines)

    #print mlcs


    code = re.sub(alc_re, '', lines)
    comt_len = len(''.join(slcs)+''.join(mlcs))
    code_len = len(code)
    # print("\n\nMetrics: {}, {}, {}, {}, {}, {}\n\n".format(len(slcs), len(mlcs), len(''.join(slcs)), len(''.join(mlcs)), comt_len, code_len))
    meta = [len(slcs), len(mlcs), len(''.join(slcs)), len(''.join(mlcs)), comt_len, code_len]
    return meta

def analyze_dirs(directories):
    if(len(directories) == 0):
	return

    metrics = []

    for dir in directories:
        filename, file_extension = os.path.splitext(dir.name)
        #print 'Filename: %-30s Ext: %-12s Type: %-10s Path: %-10s' %(filename, file_extension, dir.type, dir.path)

    for dir in directories:

        filename, file_extension = os.path.splitext(dir.name)
	#print "DIR NAME: " + dir.name
	#print "DIR TYPE: " + dir.type

        if dir.type == "dir":
	    #print "\n\nANALYZING:" + dir.name
	    #print dir
            analyze_dirs(r.get_dir_contents(dir.path, "dev"))
	    #print "BACK TO : " + dir.name
        elif dir.type == "file":

            if dir.name.endswith(".py"):
                decoded_file_content = base64.b64decode(dir.content)

                m = parse_file_str(decoded_file_content)

                metrics.append({'name': dir.name,
                        'ext': file_extension,
                        'url': dir.url,
                        'number of line Comments': m[0],
                        'number of multi-line Comments': m[1],
                        'size of line comments': m[2],
                        'size of multi-line Comments': m[3],
                        'size of Comments': m[4],
                        'size of Code': m[5]
                        })

        for file in metrics:
            for m in file:
                print("{}: {}".format(m, file[m]))
            print("\n")

g = Github("githealthtestuser","pass1234!")

for repo in g.get_user().get_repos():
    #File in githealthtestuser
    print repo.name
    repo.edit(has_wiki=False)

#Search Repository
r = g.legacy_search_repos("ghdata")[0]
#Url and owner name. 
print r.url
print r.owner
print r.get_archive_link("zipball")

# print "\n\nANALYZING:root" 

dirs = r.get_dir_contents("", "dev")
analyze_dirs(dirs)

# urllib.urlretrieve(r.get_archive_link("zipball"), r.name + ".zip")
