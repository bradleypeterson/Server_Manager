# Server_Manager
# Project Overview
A project that enables faculty at Weber State to track and manage Projects and Servers via web application.

### Admin
Admin can create projects, servers, users and groups. Admin have full CRUD operations over these objects. 

### Users
Users may register or login using the provided credentials and create/manage their own projects and servers. The user fills out the required information in the project form and submits it; from there, they are given full CRUD operations for their projects. 

### Technology Used
This project uses the Python/Django framework along with SQLite for database operations.

# Getting Started

## Dependency Setup
This project was made using the Django web framework. To get started, make sure you have an updated version of python. If not, you can download it from https://www.python.org/downloads/

Once python is installed, a virtual environment will need to be created.

From the project root, run one of the following commands in the terminal to create the virtual environment:
Note: If "python" is not recognized, use "python3".

Mac/Linux:

`python -m venv .venv`

Windows:

`python -m venv C:\path\to\project\.venv` * replace with the path to your project folder

Now from the same directory, run one of the following commands to activate the virtual environment:

Mac/Linux:

`source .venv/bin/activate`

Windows:

`.\.venv\Scripts\activate.bat`

After a virtual environment is set up, the packages are ready to be installed.

From the project root, run `pip install -r requirements.txt` from the terminal.
Note: If "pip" is not recognized, use "pip3".

## Running the project
To run the project, clone the repository and open the project with an IDE. We used Pycharm from Jetbrains, which is free for students and can be downloaded here https://www.jetbrains.com/pycharm/.

Next, navigate to the correct folder in the terminal (the one that contains the manage.py file) and run `python manage.py migrate --run-syncdb`.
Note: If "python" is not recognized, use "python3".

(if the previous command fails, make sure the required packages are installed. If not this can be done by running `pip install PACKAGENAMEHERE` in the terminal)

Next, run `python manage.py makemigrations` to make the migrations then finally run "python3 manage.py migrate". Once changes are migrated you should see a similar output in your terminal.
<img width="602" alt="image" src="https://user-images.githubusercontent.com/90224390/207728970-a2e1614a-102b-4d81-b970-b076af9ad222.png">

After the migrations are successfully applied, run `python manage.py createsuperuser` in the terminal, then follow the instructions to create an admin user.
Note: For security purposes, the password will not be displayed as you enter it.
<img width="649" alt="image" src="https://user-images.githubusercontent.com/90224390/207729468-540b8a55-ac34-4d47-835e-5464a45e951b.png">

After the migrations have been applied and a super user has been created, run `python3 manage.py runserver` and if everything was successful, the project should start and be hosted on http://127.0.0.1:8000. 
<img width="960" alt="image" src="https://user-images.githubusercontent.com/90224390/207729894-c3b98aa6-b611-42f6-9183-ba00774ba089.png">

From there you can go to http://127.0.0.1:8000/admin and login with your super user. This will show you all the database tables and allow you to make users with different roles to test the project.
<img width="960" alt="image" src="https://user-images.githubusercontent.com/90224390/207730195-2234f81e-1544-40a2-84b3-2e8c796f49b0.png">

# Troubleshooting
Occasionally, the django framework does not properly update the models and database when making updates to the Django models. The cause is unknown.
This results in being presented with several error messages such as certain tables (E.G. "group_TestUser) not being found. When this happened, there are several workarounds that can be attempted:
## 1) Specifc App Migrations
Open the terminal and apply the migrations to a specific app, E.G. `python manage.py makemigrations group`. This will typically fix the problem where a specific model doesn't get updated with the normal migrations command.
## 2) Sync Database
Open the terminal and type `python manage.py migrate --run-syncdb`
## 3) Delete Database (Loss of user accounts)
If the above 2 fail, you can try deleting the db.sqlite3 file and repeating steps 1 and 2. Please note that this will remove all user accounts from the database.

# Project Priorities
### Tier 1 </br>
- Fully functional Front End ✅
- Working Models ✅
- User Authentication (Salt and Hash) ✅
- Register Page ✅
- Generate list of active servers for auditors ✅
- Required data fields for servers ✅
- Logout ✅
### Tier 2 </br>
- Ping servers ✅
- Password Reset ✅
- Get rid of redundant code ✅
### Tier 3 (Beyond scope for semester) </br>
- Custom Data Fields for Servers 
- Code testing
- More granular permissions (grant read/update separately)
### Bugs:</br>
???

🐺