from github import Github

g= Github("githealthtestuser","pass1234!")

for repo in g.get_user().get_repos():
    #File in githealthtestuser
    print repo.name
    repo.edit(has_wiki=False)

#Search Repository
r = g.legacy_search_repos("DoSOCSv2")[0]
#Url and owner name. 
print r.url  
print r.owner
print r.get_archive_link("zipball") #get archive link chose zip format
urllib.urlretrieve(r.get_archive_link("zipball"), r.name + ".zip") #this download as a zip file and save zip file name same as file that we try to download.
