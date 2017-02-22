Luizalabs Employee Manager 
-
Luizalabs Employee Manager is an application to manage employees' information, such as name, e-mail and department using Python and the Django web framework.

>It's **flexible** because it gives the developer total control over the XML.
It's **fast** because it uses *memory mapping*,  *xpath* and no classes.
It's **simple** because uses convention over configuration, keeps everything else explicit and centralizes the customization effort in only one file for each client.

Luizalabs Employee Manager handles *crontab configuration*, remote logging with [Logentries](https://logentries.com/), download and upload of files.


### Architecture

#### jake.sh (entry point)
Luizalabs Employee Manager's entry point is `jake.sh`, located in the root directory. It requires only the name of the parser (normally the apiKey). The logical execution is:

1. Dynamically loads the parser file, that contains the configurations for this client;
2. Updates the crontab entry;
3. Downloads the XML;
4. Calls the XML reader, passing the parser as an argument, which in turn returns an generator of well-formed JSON products;
5. Products are saved in a compressed file;
6. Both JSON and XML (also compressed) are uploaded to S3;
7. The local JSON and XML files are deleted.

#### xml_reader.py (core processing)
The file `xml_reader.py` (located in `modules`) does the heavy lifting:

1. Splits the incoming XML (with possibly lots of GB)  into several ones (with a few KB), each containing only the SKUs related to one product;
2. Calls `make_product` (the customization part), passing an lxml.etree.ElementTree instance with the root node of each small XML and yields the result (hence it's a generator).

#### parser (customization)

Each client must have its own specific parser. The parsers are located in the `parsers` directory and named after their apiKeys (e.g.: `parceiroambev.py`).

To query through the XML, it's recommended to use xpath ([here's a good tutorial](http://www.w3schools.com/xsl/xpath_syntax.asp)) for it's expressiveness and simplicity.

Below there is an excerpt of a parser for 'parceiroambev':

    """Configurations as constants"""
    from .lib.ez import ezpath
    
    XML_ENDPOINT = 'http://homolog.parceiroambev...'
    ITEM_TAG = 'item'
    GROUP_TAG = 'item_group_id'
    CRON = '30 * * * *'

    """Callback function"""
    def make_product(root):
      skus = ezpath(root, '/rss/channel/item'))
      product = {}
      (...) # build a well-formed product
      return product

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
