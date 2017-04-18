# Mac Instalation Instructions

## Dependencies
Development Operating System is MacOS Sierra Version 10.13.3 with the following specs:
- All updates realease up to January 2017  
- CPU: 2.6 GHz
- SSD: 128 GB
- RAM: 8 GB

---
## Instalation and Setup

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
