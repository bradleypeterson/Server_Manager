# Server_Manager
# Project Overview
A project that enables instructors and students at Weber State to track and manage Projects and Servers via web application.
### Admin
Instructors can create courses, create groups within courses, and generate student credentials. Instructors have full CRUD operations over these objects. 
Instructors can provide the generated credentials to students within groups to login. Instructors are able to view any projects that are created from any student within a group. 

### Faculty
Students may login using the provided credentials and create/manage their own project(s). The student fills out the required information in the project form and submits it; from there, they are given full CRUD operations for their projects. 

### Technology Used
This project uses the Python/Django framework along with SQLite for database operations.
<img src="/images/Instructor_Home.PNG" width="50%" height="50%">

# Getting Started

## Installing python and django
This project was made using the Django web framework. To get started, make sure you have an updated version of python. If not, you can download it from https://www.python.org/downloads/

Once python is installed, Django needs to be installed.

On Mac or Linux operating systems, run "pip3 install django" from the terminal.
Note: If "pip3" is not recognized, use "pip".

On Windows, run "pip3 install django" from the command line, then add the script path to your environment variables.

Other libraries needed are sweetify and bcrypt which can be installed with "pip3 install sweetify" and "pip3 install bcrypt"

## Running the project
To run the project, clone the repository and open the project with an IDE. We used Pycharm from Jetbrains, which is free for students and can be downloaded here https://www.jetbrains.com/pycharm/.

Next, navigate to the correct folder in the terminal (the one that contains the manage.py file) and run "python3 manage.py migrate --run-syncdb".
Note: If "python3" is not recognized, use "python".

(if the previous command fails, make sure the required packages are installed. If not this can be done by running "pip3 install PACKAGENAMEHERE" in the terminal)

Next, run "python3 manage.py makemigrations" to make the migrations then finally run "python3 manage.py migrate". Once changes are migrated you should see a similar output in your terminal.
<img width="602" alt="image" src="https://user-images.githubusercontent.com/90224390/207728970-a2e1614a-102b-4d81-b970-b076af9ad222.png">

After the migrations are successfully applied, run "python3 manage.py createsuperuser" in the terminal, then follow the instructions to create an admin user.
Note: For security purposes, the password will not be displayed as you enter it.
<img width="649" alt="image" src="https://user-images.githubusercontent.com/90224390/207729468-540b8a55-ac34-4d47-835e-5464a45e951b.png">

After the migrations have been applied and a super user has been created, run "python3 manage.py runserver" and if everything was successful, the project should start and be hosted on 127.0.0.1:8000. 
<img width="960" alt="image" src="https://user-images.githubusercontent.com/90224390/207729894-c3b98aa6-b611-42f6-9183-ba00774ba089.png">

From there you can go to 127.0.0.1:8000/admin and login with your super user. This will show you all the database tables and allow you to make users with different roles to test the project.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/90224390/207730195-2234f81e-1544-40a2-84b3-2e8c796f49b0.png">

# Troubleshooting
Occasionally, the django framework does not properly update the models and database when making updates to the Django models. The cause is unknown.
This results in being presented with several error messages such as certain tables (E.G. "group_TestUser) not being found. When this happened, there are several workarounds that can be attempted:
## 1) Specifc App Migrations
Open the terminal and apply the migrations to a specific app, E.G. "python manage.py makemigrations group". This will typically fix the problem where a specific model doesn't get updated with the normal migrations command.
## 2) Sync Database
Open the terminal and type "python manage.py migrate --run-syncdb"
## 3) Delete Database (Loss of user accounts)
If the above 2 fail, you can try deleting the db.sqlite3 file and repeating steps 1 and 2. Please note that this will remove all user accounts from the database.

# Project Priorities
### Tier 1 </br>
-Fully functional Front End ✓ </br>
-Working Models ✓</br>
-User Authentication (Salt and Hash) ✓</br>
### Tier 2 </br>
-Professors can view student's projects and details ✓</br>
-Student's can create projects and their details ✓</br>
-Professors have full CRUD operations for Courses, groups, and user credentials ✓</br>
-Students have full CRUD operations for their projects ✓</br>
### Tier 3 (Beyond scope for semester) </br>
-Functionality for students to upload files required for containerizing projects </br>
-Collaborate with Weber IT to get a proper server set up for hosting the project </br>
-Email student credentials to student once generated by the professor (Currently just displays them to the professor to share) </br>
-Docker Containerization and deployment for working web app </br>
### Bugs:</br>
-User can switch ID and see another student's page </br>
-A confirmation message is sent even if deleting/updating fails </br>
