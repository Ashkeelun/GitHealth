##Title: GitHealth
##Background:
This system is intended to be an expansion, or extension of https://github.com/OSSHealth/ghdata. This repository looks to identify and evaluate how to acquire a repo's health and sustainability related metrics, inline with the direction of GHData. This system will be extending upon the data model and schema being used by GHData as needed.

##Goal in Context:
The user provides a URL to GitHub repository for a community that they want to learn about. The software returns metrics that indicate the health and sustainability of the repository.

##Triggers:
1- A user seeks an open source solution and assesses the health and sustainability of an open source community before getting approval to engage or contribute for that project.
2- Manager could identifies project information that associated documentation information.
##Actors:
1- Manager
2- Employees
3- Contributors

##Preconditions:
1- A user provides URL to a GitHub repository.
2- Given URL GitHub repository has to be exists.
3- A used has access to view metrics of that repository.

##Main Success Scenario:
1- All metrics that can be computed from the provided repository are displayed.

##Failed End Condition:
1- The given URL non exists, and could not find GitHub repository, metrics cannot be calculated. And gives error message that that repository is not exist. 
2- The given repository does not have parsable file, so cannot be calculated.
3- The given repository does not have enough data for metrics to be computed.
4- The user does not have access to view that metrics on that repository.

