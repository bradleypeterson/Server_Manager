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

## Running the project
To run the project, clone the repository and open the project with an IDE. We used Pycharm from Jetbrains, which is free for students and can be downloaded here https://www.jetbrains.com/pycharm/.

Next, navigate to the correct folder in the terminal (the one that contains the manage.py file) and run "python3 manage.py migrate --run-syncdb" 

Next, run "python3 manage.py makemigrations" to make the migrations then finally run "python3 manage.py migrate"

After the migrations are successfully applied, run "python3 manage.py createsuperuser" in the terminal, then follow the instructions to create an admin user.

After the migrations have been applied and a super user has been created, run "python3 manage.py runserver" and if everything was successful, the project should start and be hosted on 127.0.0.1:8000. 

From there you can go to 127.0.0.1:8000/admin and login with your super user. This will show you all the database tables and allow you to make users with different roles to test the project. 
