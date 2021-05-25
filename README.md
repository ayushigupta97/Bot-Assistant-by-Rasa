# Course-Expertise-Assistance-using-Rasa
Personal Assistant

## Table of Contents
*[Introduction](#general-info)

*[Technologies](#technologies)

*[Setup](#setup)

*[Commands](#commands)

*[Specifications](#specifications)
## Introduction
The aim of the project is to build a personal assistant suggesting some tutorials as well as contact details of the expertise of that field.
## Technologies
- Python 3.7.9
- Rasa 
- MongoDB
## Setup
To run this project, we need

- Server setup by Rasa
- Server setup by MongoDB
- Sublime Text Editor or any Text Editor
## Commands
Follow the commands in order to run the assistant.

- Open Command Line enter 'mongod'(to run mongodb server).
- Go to the specific location of project in command line using cd path.
- Enter command 'rasa run actions'(to start the rasa server).
- Enter command 'rasa train'(to train the build model).
- Enter command 'rasa shell'.
- Talk to your bot :)
## Specifications
Modules and important functionalities of project are:

- MongoDB Database named as 'exprt-details' is used having details such as name, emailId and contact of the expertise of specific technology.
- Bot is giving some options in which you might be having some problems and then giving back the user tutorials of that technology as well as details of expertise.
  


