# Project 1 - Rainy Day


Query for basic information about cities and towns in United States as well as weather information. You can leave a comment on every location. You are also able to query for location data via website's API access.

As I only have location data of United States for now, I'm working for getting South Korea's data as well. I politely ask for your understanding.

Only raw SQL is used instead of using ORM-like syntax to understand and get a lot more sense of SQL itself. ORM will be used in Project 2.

미국에 있는 도시와 지역을 검색하고 지역 정보와 현재 날씨 정보를 알 수 있습니다. 각 지역마다 직접 코멘트를 생성할 수 있으며, 지역 정보에 대한 데이터를 API를 통해 제공하고 있습니다.

프로젝트 시작에 앞서 미국의 장소 데이터만을 갖고 개발했습니다. 한국의 모든 도시들의 좌표와 주소가 정리되어 있는 DB도 만들고 있으니, 깊은 양해 부탁드립니다.

SQL 자체의 대한 이해와 숙달을 위해 ORM 문법이 아닌 순 SQL 만을 사용하여 구현했습니다. ORM은 Project 2 에서 사용할 것입니다.


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
http://[address]/api/location/10002

    {
        "City": "NEW YORK", 
        "Latitude": 40.71, 
        "Longitude": -73.99, 
        "Population": 81410, 
        "Zipcode": 10002
    }

```
## Notes
Connecting to the database over SSL is required. So make sure your client environment use an SSL connection.

## Used languages and tools
* Languages: Python 3.7, JavaScript ES6, PostgreSQL 10.5, HTML, CSS
* Frameworks and Libraries: Flask, jQuery, Bootstrap
