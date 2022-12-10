# Server_Manager
A project that enables professors and students at Weber State to track and manage Computer Science projects. This is done by web application.

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

