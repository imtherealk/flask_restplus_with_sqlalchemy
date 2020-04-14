# Flask Restplus with SQLAlchemy
flask_restplus와 SQLAlchemy를 이용한 web service 예시 프로젝트

## Install and start
`src/config/local.py` 파일에서 mysql 서버, 계정, DB 정보를 수정한다.

```
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@server:port/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
터미널에 아래 내용을 입력한다. 
```
pipenv install
pipenv shell
cd src
python app.py
```
http://0.0.0.0:8080/api/v1/ 로 접속한다.