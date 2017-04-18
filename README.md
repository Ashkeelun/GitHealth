# GitHealth

---
## System Description

This system is intended to be used by systems like https://github.com/OSSHealth/ghdata to aggrogate data. This system looks to identify a repo's documentation related metrics for the use by external systems. While the system aims to be platform agnostic and laguage agnostic, it is currently only able to parse Python files in repositories located on Github.

#### Supported Platforms:
 - Github
   
#### Supported File Types:
 - Python files (.py)

---
## Health Metrics

This repository will attempt to determine if it's posible to find the documentation quality in terms of a set of meterics as they relate to repository health. Currently this involves collecting the size and number of multi-line and single-line comments and compare them to the size of the code.

 - slcNum:  The number of single line comments found.
 - slcSize: The number of characters found in single line comments found.
 - mlcNum:  The number of multi-line comments found.
 - mlcSize: The number of characters found in multi-line comments found.
 - comtSize:The number of characters found across all comments.
 - codeSize:The number of characters found across all non-comment source code.

---
## License

Copyright © 2017 Chris Bane and Celal Gorgun

GitHealth is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

---
## Dependencies
Development Operating System is Ubuntu Desktop Version 16.04 with the following specs:
 - SSD: 50 GB
 - RAM: 1 GB

GitHealth Dependencies:
 - Python version 3.5.3
 - Django version 1.10.6
 - Django REST Framework version 3.6.2
 - Requests version 2.13.0

---
## Instalation and Setup

#### Ubuntu
1. Open the terminal.
2. Update and install base software by runnning the following commands:
  - sudo apt-get update
  - sudo apt-get install python3-pip
  - sudo apt-get install git python3-pip
  - sudo pip3 install virtualenv
3. Make directory for virtual enviornment by running the following commands:
  - mkdir ~/githealth
  - cd ~/githealth
4. Create the virtual enviornment by running the following commands:
  - virtualenv githealthenv
  - source githealthenv/bin/activate
5. clone the GitHealth repository to your local machine and navigate to it, with the following commands:
  - git clone git://github.com/Ashkeelun/GitHealth ~/githealth-master
  - cd ~/githealth-master/GitHealth
6. Install python dependencies for the system and migrate the database using the following commands:
  - pip install -r requirements.txt
  - python manage.py migrate

#### Instructions for [Windows](https://github.com/Ashkeelun/GitHealth/blob/Dev/docs/windows.md)

#### Instructions for [Mac](https://github.com/Ashkeelun/GitHealth/blob/Dev/docs/mac.md)

---
## Running The API

#### For Ubuntu 16.04
1. Run the Development Server
 - In CMD opened in step 1, enter the following command: python manage.py runserver
2. Click [here](http://127.0.0.1:8000/health/test/) to navigate to the API page.
3. Finally, post an API request in the following format:
    {"url":"https://github.com/OSSHealth/ghdata/tree/dev"}
    
---
## DFD

![image](https://cloud.githubusercontent.com/assets/14626151/24373848/5ffe8fbe-12f8-11e7-8668-399e27a5f0d0.png)

---
## ERD

![image](https://cloud.githubusercontent.com/assets/14626151/24486400/9bfa22f2-14cf-11e7-8e53-8e7bb8e45b99.png)

---
## [Use Case Documentaion](https://github.com/Ashkeelun/GitHealth/blob/Dev/docs/UseCase.md)

