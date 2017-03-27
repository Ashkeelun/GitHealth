# GitHealth
---
##System Description

This system is intended to be an expansion, or extention of https://github.com/OSSHealth/ghdata. This repository looks to identify and evaluate how to acquire a repo's health and sustainability related metrics, inline with the direction of GHData. This system will be extending upon the data model and schema being used by GHData as needed.

---
## Health Metrics

This repository will attempt to determine if it's posible to find the documentation quality in terms of a set of meterics as they relate to repository health.

---
## License

Copyright © 2017 Chris Bane and Celal Gorgun

GitHealth is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

---
## Dependencies

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
2. Once Python is installed install Django.
 - Open the windows command promt:
  - Click on the start menu (this is generally in the bottom left corner of the screen)
  - type the following: CMD
  - press enter to open the command prompt.
 - In the comand prompt, type the following followed by enter: pip install Django==1.10.6
3. Next install the Django REST Framework
 - In the comand prompt, type the following followed by enter: pip install djangorestframework==3.6.2
4. Next install the Requests Library
 - In the comand prompt, type the following followed by enter: pip install Requests==2.13.0

---
## DFD

![image](https://cloud.githubusercontent.com/assets/14626151/24373759/0832f1f8-12f8-11e7-82cd-ccbee2c48da8.png)

