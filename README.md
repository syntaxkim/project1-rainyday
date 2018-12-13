# Project 1 - Rainy Day (Flask)

한국어: [README_KOR.md](https://github.com/syntaxkim/project1-rainyday/blob/master/README_KOR.md)

Demo app: https://minsu-rainyday.herokuapp.com/
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot0.png)

Query for basic information about cities and towns in United States as well as weather information.



## Features

### Access location API from the database.
Go to API page, and read the simple overview.

Example Request
```
Use GET request

https://minsu-rainyday.herokuapp.com/api/locations/10002

    {
        "City": "NEW YORK", 
        "Latitude": 40.71, 
        "Longitude": -73.99, 
        "Population": 81410, 
        "Zipcode": 10002
    }


You can also access each endpoint by specifying particular information.
Supported endpoints: city, lat, long

https://minsu-rainyday.herokuapp.com/api/locations/10002/city

    {
        "City": "NEW YORK"
    }

```

### Search location information with current weather
The location page will show you the location information such as ZIP code, city name, coordinates along with current weather.
The weather information uses [Dark Sky API](https://darksky.net/dev) service.
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot1.png)
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot2.png)

### Check in a comment on every location.
Go to that location, leave a comment.\
You can also delete the comment as you want.
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot3.png)

### User authentication
Password is encrypted by PBKDF2-SHA256 algorithm.

## Notes
* Only raw SQL is used in order to understand and get a lot more sense of SQL itself. But I wrote and included [models.py](https://github.com/syntaxkim/project1-rainyday/blob/master/models.py) to refer to in case of ORM with [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/).
* The database consists of 3 tables - users, locations, comments(check-ins)
* Demo application is deployed with [Heroku](https://www.heroku.com) and due to server's automatic sleep function, a short delay could occur to reboot the application.

## Languages and Tools
* Languages: Python 3.7, SQL, HTML, CSS, JavaScript ES6
* Frameworks and Libraries: Flask, Bootstrap, jQuery
* DBMS: PostgreSQL
