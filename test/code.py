from github import Github

g= Github("githealthtestuser","pass1234!")

for repo in g.get_user().get_repos():
    #File in githealthtestuser
    print repo.name
    repo.edit(has_wiki=False)

#Search Repository
r = g.legacy_search_repos("DoSOCSv2")[0]
#Url and owner name. 
r.url
r.owner

