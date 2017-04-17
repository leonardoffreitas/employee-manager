Luizalabs Employee Manager 
-
Luizalabs Employee Manager is an application to manage employees' information, such as name, e-mail and department using Python and the Django web framework.


### Architecture

#### python manager.py runserver
Luizalabs Employee Manager's entry point is `manager.py`, located in the root directory. It requires only the django command to start the server. Also, we have a interface to manage the employees data:

- A Django Admin panel to manage employees' data
- An API to list, add and remove employees

## Getting Started

If you're comfortable getting up and running from a `git clone`, this method is for you.

If you clone the GitHub repository, you will need to install some libs.

The [master](https://github.com/leonardoffreitas/employee-manager.git) branch which contains the latest release.

### Dependencies
Using `apt-get`:
```
sudo apt-get install 	\
   python            	\
   python-pip       	\
   build-essential &&
pip install Django   
```   
### How to use

The entry point is `manager.py`, located in the root directory. You can start your server by typing `python manage.py runserver`, press enter. The server will be available on port 8000.
The follow screen will be showed on terminal:


```
Performing system checks...

System check identified no issues (0 silenced).
March 01, 2017 - 19:44:02
Django version 1.10.5, using settings 'employees.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

To close, you can press the keys `ctrl` + `c` on your keyboard, like said on the screen.

>To start the server on a different port, type the port in the end of the command - 8080, for example:
`python manage.py runserver 8080`

#### Employee Manager Interface

To login you need to create a superuser - (for default exist the user: "admin" - and password: "luizalabsdjango") - a user who has control over everything on the site. Go back to the terminal and type `python manage.py createsuperuser`, press enter and enter your username (lowercase, no space), email address and password when they are requested. Do not worry that you can not see the password you are typing in - this is how it should be. Just enter it and press 'Enter' to continue. The output should look like this (where Username and Email should be yours):

```
python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

So start the server: `python manage.py runserver`.
Go to your browser and login with the superuser credentials you chose, you should see the Django admin control panel. The server will be available on port 8000 by the URL: http://localhost:8000/admin/.
You will be able to manage your employees, also create new users to the system and manager them.


#### API (RESTful URLs and actions)

On the terminal, type `python manage.py runserver`, press enter. The server will be available on port 8000 read do listen.
Again. The screen will be showed.

```
Performing system checks...

System check identified no issues (0 silenced).
March 01, 2017 - 19:44:02
Django version 1.10.5, using settings 'employees.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Those are the actions applied to use the API. RESTful principles provide strategies to handle CRUD actions using HTTP methods mapped as follows:

```
GET /employee - Retrieves a list of employees
GET /employee/12 - Retrieves a specific employee by ID
GET /employee/Renato - Retrieves a specific employee by Name
POST /employee - Creates a new employee
DELETE /employee/12 - Deletes employee ID #12
DELETE /employee/Renato - Deletes employee Name Renato
```

Below there is an example of each request:

```
ADD - curl -X POST -d '{"name":"Leonardo", "email": "leonardo@luzialabs.com", "department": "Dev"}' http://localhost:8000/employee/
LIST - curl -X GET -H "Content-Type: application/javascript" http://localhost:8000/employee/
GET - curl -X GET -H "Content-Type: application/javascript" http://localhost:8000/employee/leonardo
GET - curl -X GET -H "Content-Type: application/javascript" http://localhost:8000/employee/1
REMOVE - curl -X DELETE -H "Content-Type: application/javascript" http://localhost:8000/employee/1
REMOVE - curl -X DELETE -H "Content-Type: application/javascript" http://localhost:8000/employee/leonardo
```

Have fun!
