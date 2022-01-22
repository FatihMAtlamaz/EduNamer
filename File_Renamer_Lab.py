# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:35:36 2022

@author: fmatl

Fatih Atlamaz | Ohm Patel | Wesley Schuh | Marley Mack
1/18/2022
FHS Mudsock Hackathon
"""
#This package is to access the system to create and store files
import os
#This package is to access and set the file name as the current time and date
from datetime import date
#This package is used to sort files based on a given parameter
from pathlib import Path
#This package is used to create a GUI for the user to see and interact with
import PySimpleGUI as sg 

"""
The overall purpose of this code is to supplement Canvas in order to better organize assignments.
This project will implement the use of another code which is not shown in this project to access
the Canvas API and pull the name of the student, assignment, and date submitted. Thus 
in order to actually run the project, example code is used to simulate that information.
This information is then used to rename the file and make a new folder with the assignment name
if it doesn't already exist. The newly renamed files are then added to the new folder.
For example, if a student named Billy Bob submitted an assisgnment titled Food Truck Lab but the
file was named Document 1 it would rename the file as "Billy Bob + Food Truck Lab + 2022-01-21"
and then put it in a folder named Food Truck Lab.
"""

"""
System grabs information from Canvas (Cannot be implemented due to the fact that we don't have access to Canvas API)
Student first name, student last name, assignment name, date submitted.
Grabs the file from the student. 
"""


studentFirstName = "Amr"
studentLastName = "Lee"

today = date.today()

"""
The user needs to put their downloads folder's path here or the path to the folder that receives the downloaded files.
"""
userDownloadsDirectory = "C:\\Users\\fmatl\\Downloads" 

####GUI Code
#Sets the color of the theme
sg.theme('LightGrey4')

layout =[
    [sg.Text("Welcome to EduNamer!")],
    [sg.Text("Please insert assignment name")],
    [sg.Text("Assignment", size =(15, 1)), sg.InputText('', size=(15,1), key='input_name')],
    [sg.Submit(), sg.Cancel()]
]

# Create the window
window = sg.Window("EduNamer", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Submit" :
        assignmentName = values['input_name']
        break
    elif event == "Cancel" or event == sg.WIN_CLOSED:
        break

event, values = window.read()
window.close()

#Creates a folder for the assignment if the folder does not yet exist.
'''
User inputs the path in which they want the folder created. For example, a computer science teacher, who teaches
AP CS A, could put the path directory for a folder that holds all of the AP CS A files.
Note: Keep the "r"!!!
'''
currentClassPath = r"C:/Users/fmatl/OneDrive/Documents/12th Grade/AP CS A/" 

newFolderPath = str(currentClassPath) + str(assignmentName) 
print(str(currentClassPath) + str(assignmentName))
if not os.path.exists(newFolderPath ):
    os.makedirs(newFolderPath)    
    
#Changes the directory to the downloads file because that's where the downloaded files are stored.
os.chdir(userDownloadsDirectory)

sortedListFiles = []
sortedListFiles = sorted(Path(userDownloadsDirectory).iterdir(), key=lambda f: f.stat().st_ctime)
#print(sortedListFiles)
newestFile = str(sortedListFiles[-1])
print(newestFile)
#index = lastFile.index("\\Downloads\\")
#oldFileName = str(lastFile[25:])
#print(oldFileName)

#New variable "fileType" will determined if the file is a docx, csv, txt, etc...
fileType = newestFile

countPeriod = 0
for x in fileType:
    if (x == "."):
        countPeriod = countPeriod + 1

for x in range(countPeriod):
    index = fileType.index(".")
    fileType = fileType[index+1:]
    
#Creates the new file's name
newFileName = newFolderPath + "\\" + str(studentFirstName) + " " + str(studentLastName) + " + " + str(assignmentName) + " + " + str(today) + "." + str(fileType)
print("New file name: " + str(newFileName))

#Renames the file
os.rename(newestFile, newFileName)
 
print("File renamed!")

