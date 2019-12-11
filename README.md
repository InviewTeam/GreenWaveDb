# Prerequirements

Prepare .env file inside 'app/':
```
DBUSER=<<name of database user>>
DBPASS=<<name of user password>>
DBHOST=<<database host>>
DBNAME=<<database name>>
```

Install Python3 and Postgres and then run:
```
sudo apt-get install python3-pip
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Run

Go to 'app/' and run:

```
flask run
```

# Routes

Server processes post request to adding new data and get requests to receive all records or records per specified period.

In order to add the record, send post request to:
```
http://[[SERVERHOST]]/add/record
```

The body:

```
light_id: integer
interval: integer
date: string[YYYY-MM-DD hh:mm:ss]
success_counter: integer
fail_counter: integer
```

In order to get all records, send get request to:
```
http://[[SERVERHOST]]/get/all
```

In order to get records per period, send get request to:
```
http://[[SERVERHOST]]/bytime?from=string[YYYY-MM-DD hh:mm:ss]&to=string[YYYY-MM-DD hh:mm:ss]
```

For instance:

```
http://0.0.0.0:5000/get/bytime?from=2017-09-06%2009:45:28&to=2017-09-06%2009:45:28
```
