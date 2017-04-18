# Windows Instalation Instructions

## Dependencies
Development Operating System is Windows 10 64bit with the following specs:
- All Windows updates realease up to March 2017  
- CPU: 2.6 GHz
- SSD: 256 GB
- RAM: 8 GB

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
