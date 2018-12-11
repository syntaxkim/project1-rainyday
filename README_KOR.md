# Project 1 - Rainy Day (Flask)

English: [README.md](https://github.com/syntaxkim/project1-rainyday/blob/master/README.md)

![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot0.png)

미국에 있는 도시와 지역을 검색하고 지역 정보와 현재 날씨 정보를 알 수 있습니다.

프로젝트 시작에 앞서 미국의 장소 데이터베이스만을 갖고 개발했습니다.


## 기능

### 장소 정보를 제공하는 API
API 페이지에서 개요를 확인 후 사용이 가능합니다.

예시
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

### 장소 검색을 통한 지역 정보와 현재 날씨 정보
장소 페이지에서 현재 날씨와 함께 각 장소의 집 코드, 도시 이름, 좌표 등을 확인할 수 있습니다.
날씨 정보는 [Dark Sky API](https://darksky.net/dev) 를 사용하여 제공합니다.
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot1.png)
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot2.png)

### 코멘트 생성
원하는 장소에 댓글을 남길 수 있습니다.\
댓글 삭제도 가능합니다.
![main](https://raw.githubusercontent.com/syntaxkim/project1-rainyday/master/screenshots/screenshot3.png)

### 사용자 인증
비밀번호는 PBKDF2-SHA256 알고리즘을 통해 암호화됩니다.

## 기타
* SQL 자체의 대한 이해와 숙달을 위해 순 SQL만을 사용했습니다. 그러나 [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)를 사용한 ORM 시 참고를 위해 [models.py](https://github.com/syntaxkim/project1-rainyday/blob/master/models.py) 파일을 별도로 작성 및 추가하였습니다.
* 데이터베이스는 총 3개의 테이블로 구성했습니다 - 사용자, 장소, 코멘트
* 데모 애플리케이션은 [Heroku](https://www.heroku.com)에서 호스팅 됩니다. 서버의 자동 휴면 기능으로 인해 접속 시 약간의 지연이 있을 수 있습니다.

## 사용 언어 및 도구
* Languages: Python 3.7, SQL, HTML, CSS, JavaScript ES6
* Frameworks and Libraries: Flask, Bootstrap, jQuery
* DBMS: PostgreSQL
