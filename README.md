Luizalabs Employee Manager 
-
Luizalabs Employee Manager is an application to manage employees' information, such as name, e-mail and department using Python and the Django web framework.


### Architecture

#### python manager.py runserver
Luizalabs Employee Manager's entry point is `jake.sh`, located in the root directory. It requires only the name of the parser (normally the apiKey). The logical execution is:

- A Django Admin panel to manage employees' data
- An API to list, add and remove employees

## Getting Started

If you're comfortable getting up and running from a `git clone`, this method is for you.

If you clone the GitHub repository, you will need to build a number of assets using grunt.

The [master](https://github.com/leonardoffreitas/employee-manager.git) branch which contains the latest release.

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
Except for XML_ENDPOINT, ITEM_TAG, GROUP_TAG, CRON and the `make_product` method, everything else is up to the developer!

Have fun!

### Dependencies
Using `apt-get`:
```
sudo apt-get install \
   python3           \
   python3-pip       \
   build-essential   \
   libssl-dev  
```   
Other dependencies are installed automatically (using pip3) by `jake.sh`

You will also need platform credentials (stored in the `PLAT_USER` and `PLAT_PASSWORD` environment variables) and rw access to the `s3://custom-feeds` bucket.

### How to use
1. Execute jake as so: `./jake.sh $parser_module`

## Testing

Run `./jake.sh --test` to run unit tests and validation sets (more on validation sets below).

### Validation sets

To ensure that a parser's output is consistent even with changes in parser code, jake can run the output of the parsers' make\_product() calls against /validation sets/, which hold historical outputs of make\_product() against a set of inputs.

When you create a new parser and is confident that it's working OK, it's a good idea to also create a validation set and upload to the validation set s3 (at 's3://custom-feeds/validation_sets/'). To do this, run:

```./jake.sh --validation create $apiKey``` 

This will create a validation set for `$apiKey` in `validation_sets/` and upload to the s3 validation set bucket. In the future, if you want to check if a change in the code caused an unintentional side-effect, you can run:

```./jake.sh --test```

...to run unit tests and validation sets for all apiKeys. Other useful commands include:
```
# Run validation sets only, without unit tests
./jake.sh --validation run

# Run validation sets for apikeys matching a regex
./jake.sh --validation run '.*melissa.*'

# Run validation sets for at most 500 products per apikey
./jake.sh --validation run '.*' 500

# To update a validation set (e.g. because of an intended change in parser output), you can delete a local validation set and run validation set creation again
rm validation_sets/$apikey.gz && ./jake.sh --validation create $apiKey
```

Check `./jake.sh --help` for more usage tips on tests and validation commands.
