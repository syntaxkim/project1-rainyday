# Project 1 - Rainy Day (Flask)

English: [README.md](https://github.com/syntaxkim/project1/blob/master/README.md)

미국에 있는 도시와 지역을 검색하고 지역 정보와 현재 날씨 정보를 알 수 있습니다. 각 지역마다 직접 코멘트를 생성할 수 있으며, 지역 정보에 대한 데이터를 API를 통해 제공하고 있습니다.

프로젝트 시작에 앞서 미국의 장소 데이터만을 갖고 개발했습니다. 한국의 모든 도시들의 좌표와 주소가 정리되어 있는 DB도 만들고 있으니, 깊은 양해 부탁드립니다.

SQL 자체의 대한 이해와 숙달을 위해 ORM 문법이 아닌 순 SQL만을 사용하여 구현했습니다. ORM은 Project 2에서 사용할 것입니다.


## 기능

### 회원 가입, 로그인, 장소 검색
장소 검색을 위해서는 계정을 만들고 로그인을 해야합니다.\
계정 생성 시 비밀번호는 Postgres의 'pgcrypto' module을 사용해 암호화 됩니다.\
(암호화에 사용되는 알고리즘은 MD5 입니다.)

### 장소 정보 (데이터베이스)
장소 페이지에서 각 장소의 집 코드, 도시 이름, 좌표 등을 볼 수 있습니다.

### 현재 날씨 정보 (API)
장소 페이지에서 온도, 습도, 풍속 같은 현재 날씨 정보를 볼 수 있습니다.\
날씨 정보는 [Dark Sky API](https://darksky.net/dev) 를 사용하여 제공합니다.

### 코멘트 생성
원하는 장소에 댓글을 남길 수 있습니다.\
댓글 삭제도 가능합니다.

### 장소 정보를 제공하는 API
API 페이지에서 개요를 확인 후 사용이 가능합니다.\

예시
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
## 기타
* 애플리케이션은 [Heroku](https://www.heroku.com)에서 호스팅 됩니다.
* 서버의 자동 휴면 기능으로 인해 최초 접속 시 약간의 지연이 있을 수 있습니다.
* 데이터베이스 연결에 SSL 사용을 강제 설정했습니다. 접속 환경에서 SSL 사용이 가능해야 합니다. (대부분 기본적으로 사용 가능)
* 데이터베이스는 총 3개의 테이블로 구성했습니다 - 사용자, 장소, 코멘트

## 사용 언어 및 도구
* Languages: Python 3.7, JavaScript ES6, PostgreSQL 10.5, HTML, CSS
* Frameworks and Libraries: Flask, jQuery, Bootstrap
