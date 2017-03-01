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

If you clone the GitHub repository, you will need to build a number of assets using grunt.

The [master](https://github.com/leonardoffreitas/employee-manager.git) branch which contains the latest release.

### Dependencies
Using `apt-get`:
```
sudo apt-get install 	\
   python            	\
   python-pip       	\
   build-essential   	\
   pip install Django   
```   
### How to use

#### API (RESTful URLs and actions)

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

1. Execute jake as so: `./jake.sh $parser_module`

Have fun!

## Testing

Run `./jake.sh --test` to run unit tests and validation sets (more on validation sets below).

