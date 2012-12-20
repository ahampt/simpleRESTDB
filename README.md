simpleRESTDB
============

Django based webapp to store/retrieve simple key/value pairs in a database through HTTP calls with JSON

## Installation

Install simpleRESTDB yourself to contribute to the site and use it for your own needs. There's plenty to add and fix.

### Dependencies

1. Install [Python](http://www.python.org/) 2.7.3+.

2. Install [setuptools](http://pypi.python.org/pypi/setuptools) and [MySQL-Python](http://sourceforge.net/projects/mysql-python/) python modules in this order. Let me know if you need any of the packages as I think some of them have lost support.

3. Install Apache Stack for [Linux](http://www.unixmen.com/install-lamp-with-1-command-in-ubuntu-1010-maverick-meerkat/), [Windows](http://www.wampserver.com/en/), or [Mac](http://www.mamp.info/en/index.html) if you don't have Apache and MySQL.

4. Install [Django](https://www.djangoproject.com/download/) 1.4.3

### Configuration

1. Download the project code from master or fork if you plan on possibly contributing later.

2. Create your own settings file to preserve the global file.
    * Copy local_settings.template where it lies and name the copy "local_settings.py" (**Make sure you use this exact filename**).

3. Configure the settings page to work with your system **All changes should be made in the local_settings.py file and not settings.py**.
    * Create DB using [phpmyadmin](http://127.0.0.1/phpmyadmin) with whatever name you want, just be sure to put the name of it here. (Set the collation to utf8_bin)
    * Set your own username and password for said database. Leave password blank ('') if no password.
    * Set the time zone correctly for you or leave alone.
    * Change the PREFIX_URL as you see fit (This means to get to the site you will have to go to http://localhost/PREFIX_URL)
    * Change LOGGING_DIR to wherever you have a folder to keep all of the log files from this project (Default is to folder in /var/log/pref). Be sure that the folder already exists or you make it beforehand.
    * Make any other changes that the template describes if desired.

### Using simpleRESTDB

1. /get/all/ - No parameters needed. This simple GET request will send back all key/value pairs in the database. Example: `{key:value}`

2. /get/ - Parameters in the form of {'key_of_object_to_get' : 'Key'} where 'key_of_object_to_get' is the key of the object desired to be returned and 'Key' is the string 'Key'. The reply will be the list of key/value pairs returned if successful and errors otherwise. Example: {'key_of_object_to_get':'value','key_of_second_object_to_get':'KeyNotFound'}

3. /update/ - Parameters in the form of {'key' : 'value'}. All parameters passed in will be updated accordingly. If a key/value pair does not already exist it will be created. Will return what is passed in unless failure. Example: {'key' : 'value', 'key2' : 'Error blah blah'}

4. /delete/ - Parameters are in the same form as /get/ function. All key/value pairs sent in will be deleted by the key sent in with reply of Deleted or KeyNotFound for the corresponding action.

* Note all parameters need to be json objects (simplet key/value pairs) and all replies will be of the same type.
* The access_password variable in the settings file are to hide this functionality from only those who know it. This is simply done by requiring that the password be in front of all requests. For example to call the /get/all/ function, a user must instead call /password/get/all/.
