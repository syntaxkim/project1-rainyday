# Project 1 - Rainy Day (Flask)

한국어: [README_KOR.md](https://github.com/syntaxkim/project1/blob/master/README_KOR.md)

Query for basic information about cities and towns in United States as well as weather information. You can leave a comment on every location. You are also able to query for location data via website's API access.

As I only have location data of United States for now, I'm working for getting South Korea's data as well. I politely ask for your understanding.

Only raw SQL is used instead of using ORM-like syntax to understand and get a lot more sense of SQL itself. ORM will be used in Project 2.


## Features

### Sign up and log in to search location
To search location, you are required to sign in. If you don't have one, just simply make a new username.\
When creating a username, your password is encrypted using Postgres module 'pgcrypto'.\
(The algorithm to encrypt is MD5-based crypt)

### Search location information (Database)
The location page will show you the location information such as ZIP code, city name, coordinates, etc.

### Current weather information (API)
The location page will show you the current weather information such as temperature, humidity, wind speed, etc.\
The weather information uses [Dark Sky API](https://darksky.net/dev) service.

### Check in a comment on a location you want
Go to that location, leave a comment.\
You can also delete the comment as you want.

### You can access location API from the database.
Go to API page, and read the simple overview.\
Example Request
```
https://minsu-rainyday.herokuapp.com/api/location/10002

    {
        "City": "NEW YORK", 
        "Latitude": 40.71, 
        "Longitude": -73.99, 
        "Population": 81410, 
        "Zipcode": 10002
    }

```
## Notes
* The application is deployed with [Heroku](https://www.heroku.com).
* Due to server's automatic sleep function, a short delay could occur following inital connection.
* Connecting to the database over SSL is required. So make sure your client environment use an SSL connection.
* The database consists of 3 tables - users, locations, comments(check-ins)

## Used languages and tools
* Languages: Python 3.7, JavaScript ES6, PostgreSQL 10.5, HTML, CSS
* Frameworks and Libraries: Flask, jQuery, Bootstrap
