# GitHealth
---
##System Description

This system is intended to be an expantion, or extention of https://github.com/OSSHealth/ghdata. This system will add a look up and evaluate a repo's license information as it relates to usability by third parties. This system will be extending upon the data model and schema being used by GHData. The extention will be used to store the repository's licence information.

---
## License

GitHealth is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

---
## Dependencies

For compatibility this system will mimic the dependencies of the GHData system, which is currently:

- Python 3.4.x
- MySQL 5.x or later version (can be on a separate machine)
- GHTorrent in database (can be installed with `ghdata install --historical` on Linux/OS X machines)
  - 50GB download, requires ~1TB free space for the database

Optional:
- Running version of GHTorrent (can be installed with `ghtorrent install`)
  - Requires Ruby and Git

Python libraries:
- All Python dependencies are handled automatically by `pip`.

---
## DFD

The data flow diagram has been made inreference to how our system relates to https://github.com/OSSHealth/ghdata.

![image](https://cloud.githubusercontent.com/assets/14626151/23136835/3d0ce546-f764-11e6-975d-ee505f5e3f53.png)
