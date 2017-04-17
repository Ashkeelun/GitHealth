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
Development Operating System is MacOS Sierra Version 10.13.3 with the following specs:
- All updates realease up to January 2017  
- CPU: 2.6 GHz
- SSD: 128 GB
- RAM: 8 GB

Development Operating System is Windows 10 64bit with the following specs:
- All Windows updates realease up to March 2017  
- CPU: 2.6 GHz
- SSD: 256 GB
- RAM: 8 GB

GitHealth Dependencies:
- Python version 3.5.3
- Django version 1.10.6
- Django REST Framework version 3.6.2
- Requests version 2.13.0

---
## Instalation and Setup

#### Mac
1. Install Python version 3.5.3 on your computer for Mac.
- Download the file called 'MacOS X 64-bit/32-bit installer' [here](https://www.python.org/downloads/release/python-353/).
- Double click on downloaded file and begin the installation process.
- Click on 'continue' button.
- On License page, it will ask 'do you agree to the terms of the software license agreement?' Click on "Agree" button.
    (if you do not agree, installation file will be automatically close.)
- On "Destination Select" page, you should select the disk where you want to install the python software.
    (Installation software requires 97.2 MB of space)
- And countinue then click on "install" button for the software to where you selected your destination to install.
2. Once Python is installed install Django version 1.10.6.
- Click on Spotlight Search symbol on top right corner of the screen.
- Type the following: Terminal
- Press enter to open the Terminal.
- In the Terminal, type the following followed by enter: pip install Django==1.10.6
3. Next install the Django REST Framework
- In the Terminal, type the following followed by enter: pip install djangorestframework==3.6.2
4. Next install the Requests Library
- In the command promt, type the following followed by enter: pip install Requests==2.13.0
5. Download a copy of the GitHealth repository to your local drive.
 - Click [here](https://github.com/Ashkeelun/GitHealth/archive/master.zip) to download a zip of the repository.
 - Double click on downloaded a zip of the repository, and it will automatically extract zip of the repository in same destination.
 
#### Windows
1. Install Python version 3.5.3 on your computer for windows 10.
 - Download the file called 'Windows x86-64 executable installer' [here](https://www.python.org/downloads/release/python-353/).
 - Right click on the downloaded file and select 'Run as Administrator' to begin the instalation process.
 - Check the box at the bottom of the screen to 'Install launch for all users'.
 - Check the box at the bottom of the screen to 'Add Python 3.5 to PATH'.
 - Click on Customize installation.
 - Check all boxes and click 'Next'.
 - Again, check all boxes.
 - Select a custom install location by clicking 'Browse'.
 - Navigate to your 'C' drive.
 - Create a new folder called 'python35'.
 - Navigate to the created folder python35 and click 'Okay'.
 - Click 'Install' to install python.
2. Download a copy of the GitHealth repository to your local C drive.
 - Click [here](https://github.com/Ashkeelun/GitHealth/archive/master.zip) to download a zip of the repository.
 - Navigate to the downloaded zip file, right-click on it and select "Extract All..." from the context menu.
 - Enter the following folder location: C:\
 - Click "Extract", to complete the installation.
3. Install all the remaining dependencies.
 - Open the windows command promt:
  - Click on the start menu (this is generally in the bottom left corner of the screen)
  - Type the following: CMD
  - Press enter to open the command prompt.
 - Navigate to the repository
  - In the command prompt, type the following followed by enter: C:
  - In the command prompt, type the following followed by enter: cd C:\GitHealth-master\GitHealth\
 - Install required dependencies
  - In the command prompt, type the following followed by enter: pip install -r requirements.txt
4. Migrate Database
 - In the command prompt, type the following followed by enter: python manage.py migrate 

---
## Running The API

#### For MacOS Sierra (10.12.3)
1. Open Terminal and navigate to the downloaded copy of the GitHealth repository.
 - Open the Terminal:
  - Click on "Spotlight search symbol" (this is generally in the top right corner of the screen)
  - type the following: Terminal
  - press enter to open the Terminal.
 -Enter the following command to navigate to the extracted repository: cd Downloads/GitHealth-master/GitHealth
2. Run the Development Server
 - In Terminal opened in step 1, enter the following command: python manage.py runserver
3. Click [here](http://127.0.0.1:8000/health/test/) to navigate to the API page.
4. Finally, post an API request in the following format:
    {"url":"https://github.com/OSSHealth/ghdata/tree/dev"}

#### For Windows 10
1. Open CMD and navigate to the downloaded copy of the GitHealth repository.
 - Open the windows command promt:
  - Click on the start menu (this is generally in the bottom left corner of the screen)
  - type the following: CMD
  - press enter to open the command prompt.
 -Enter the following command to navigate to the extracted repository: cd C:\GitHealth-master\GitHealth
2. Run the Development Server
 - In CMD opened in step 1, enter the following command: python manage.py runserver
3. Click [here](http://127.0.0.1:8000/health/test/) to navigate to the API page.
4. Finally, post an API request in the following format:
    {"url":"https://github.com/OSSHealth/ghdata/tree/dev"}
    
---
## DFD

![image](https://cloud.githubusercontent.com/assets/14626151/24373848/5ffe8fbe-12f8-11e7-8668-399e27a5f0d0.png)

---
## ERD

![image](https://cloud.githubusercontent.com/assets/14626151/24486400/9bfa22f2-14cf-11e7-8e53-8e7bb8e45b99.png)

