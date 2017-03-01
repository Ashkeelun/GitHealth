# GitHealth
---
##System Description

This system is intended to be an expantion, or extention of https://github.com/OSSHealth/ghdata. This repository looks to identify and evaluate how to acquire a repo's health and sustainability related metrics, inline with the direction of GHData. This system will be extending upon the data model and schema being used by GHData as needed.

---
## Health Metrics

This repository will attempt to determine if it's posible to find the documentation quality in terms of a set of meterics as they relate to repository health.

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

![image](https://cloud.githubusercontent.com/assets/14626151/23240839/4760d0de-f935-11e6-8d49-f37a9e99c235.png)

