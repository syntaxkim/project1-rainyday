# Project 1 - Rainy Day (Flask)

한국어: [README_KOR.md](https://github.com/syntaxkim/project1-rainyday/blob/master/README_KOR.md)

Query for basic information about cities and towns in United States as well as weather information.

As I only have location data of United States for now, I'm working for getting South Korea's data as well. I politely ask for your understanding.

Only raw SQL is used instead of using ORM-like syntax to understand and get a lot more sense of SQL itself.


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


특정 URL을 통해 기본 JSON 데이터에서 일부만 추출이 가능합니다.
city, lat, long 만 추가했습니다.

https://minsu-rainyday.herokuapp.com/api/locations/10002/city

    {
        "City": "NEW YORK"
    }

```


### Sign up and log in to search location
When creating a username, your password is encrypted using Postgres module 'pgcrypto'.\
(The algorithm to encrypt is MD5-based crypt)

### Search location information (Database)
The location page will show you the location information such as ZIP code, city name, coordinates, etc.

### Current weather information (API)
The location page will show you the current weather information such as temperature, humidity, wind speed, etc.\
The weather information uses [Dark Sky API](https://darksky.net/dev) service.

### Check in a comment on every location.
Go to that location, leave a comment.\
You can also delete the comment as you want.


## Notes
* The application is deployed with [Heroku](https://www.heroku.com).
* Due to server's automatic sleep function, a short delay could occur to reboot the application.
* Connecting to the database over SSL is required. So make sure your client environment use an SSL connection.
* The database consists of 3 tables - users, locations, comments(check-ins)

## Languages and Tools
* Languages: Python 3.7, SQL, HTML, CSS, JavaScript ES6
* Frameworks and Libraries: Flask, Bootstrap, jQuery
