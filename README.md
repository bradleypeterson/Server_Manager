# Server_Manager
# Project Overview
A project that enables instructors and students at Weber State to track and manage Computer Science projects via web application.
### Instructors
Instructors can create courses, create groups within courses, and generate student credentials. Instructors have full CRUD operations over these objects. 
Instructors can provide the generated credentials to students within groups to login. Instructors are able to view any projects that are created from any student within a group. 

### Students
Students may login using the provided credentials and create/manage their own project(s). The student fills out the required information in the project form and submits it; from there, they are given full CRUD operations for their projects. 

### Technology Used
This project uses the Pythong/Django framework along with SQLite for database operations.
<img src="/images/Instructor_Home.PNG" width="50%" height="50%">

# Getting Started

## Installing python and django
This project was made using the Django web framework. To get started, make sure you have an updated version of python. If not, you can download it from https://www.python.org/downloads/

Once python is installed, Django needs to be installed.

On Mac or Linux operating systems, run "pip3 install django" from the terminal.

On Windows, run "pip3 install django" from the command line, then add the script path to your environment variables.

Other libraries needed are sweetify and bcrypt which can be installed with "pip3 install sweetify" and "pip3 install bcrypt"

## Running the project
To run the project, clone the repository and open the project with an IDE. We used Pycharm from Jetbrains, which is free for students and can be downloaded here https://www.jetbrains.com/pycharm/.

Next, navigate to the correct folder in the terminal (the one that contains the manage.py file) and run "python3 manage.py migrate --run-syncdb"

(if the previous command fails, make sure the required packages are installed. If not this can be done by running "pip3 install PACKAGENAMEHERE" in the terminal)

Next, run "python3 manage.py makemigrations" to make the migrations then finally run "python3 manage.py migrate"

After the migrations are successfully applied, run "python3 manage.py createsuperuser" in the terminal, then follow the instructions to create an admin user.

After the migrations have been applied and a super user has been created, run "python3 manage.py runserver" and if everything was successful, the project should start and be hosted on 127.0.0.1:8000. 

From there you can go to 127.0.0.1:8000/admin and login with your super user. This will show you all the database tables and allow you to make users with different roles to test the project.

## Creating A Project
Once logged in as a student, your dashboard will display all group/individual projects. To create a new project, simply click on the button labeled “New Project” in the bottom left. You will be redirected to a new page. A form will be displayed, fill out all the information accordingly. 

Once finished, click “Save”. All information will be stored as a new project to the database. In this case, we are using sqlite.

Only students/ groups and the professor associated with the project can view it. Students can further edit and delete projects.

## Project Priorities
### Tier 1 </br>
-Fully functional Front End ✓ </br>
-Working Models ✓</br>
-User Authentication (Salt and Hash) ✓</br>
### Tier 2 </br>
-Professors can view student's projects and details ✓</br>
-Student's can create projects and details ✓</br>
-Professors have full CRUD operations for Courses, groups, and user credentials ✓</br>
-Students have full CRUD operations for their projects ✓</br>
### Tier 3 (Beyond scope for semester) </br>
-Functionality for students to upload files required for containerizing projects </br>
-Collaborate with Weber IT to get a proper server set up for hosting project </br>
-Docker Containerization and deployment for working web app </br>
### Bugs:</br>
-User can switch ID and see another student's page (I think) </br>
-A confirmation message is sent even if deleting/updating fails </br>

## What's Next?
