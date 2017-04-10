## Title: GitHealth

## Goal in Context
The user provides a URL to GitHub repository for a community that they want to learn about. The software returns metrics that indicate the health and sustainability of the repository. Metrics checks each python file in provided URL, and it gives information about documantation in these files. It shows that, how many character code and documantation used in those python files. It can help user, how clear and understandable those python files.

## Triggers
1- A user can analyze the health and sustainability of an open source community, and user can see documantation information and it will help them to engage or contribute for that project. 
## Actors
1- User <br />

## Stackholders
1- User: provides URL and access to see pyton files' documantation information in this repository.<br />
2- Repository Owner: To provide the relavant Repositories' files documantation information.<br />
3- Repository facilitator: To provide the relavant URL's repository and files in that repository.
## Preconditions
1- A user provides URL to a GitHub repository. <br />
2- Given URL GitHub repository has to be exists. <br />
3- A used has access to view metrics of that repository. 

## Main Success Scenario
1- All metrics that can be computed from the provided repository are displayed.

## Failed End Condition
1- The given URL non exists, and could not find GitHub repository, metrics cannot be calculated, and gives error message that that repository is not exist. <br />
2- The given repository does not have parsable file, so cannot be calculated. <br />
