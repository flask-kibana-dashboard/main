# 🚀 Flask-Kibana Dashboard

## 📌 프로젝트 개요

Flask와 ELK(Stack)인 Elasticsearch, Logstash, Kibana, Filebeat를 활용하여 실시간 고객 데이터를 조회할 수 있는 대시보드 애플리케이션입니다. 
사용자가 고객 번호를 입력하면 해당 데이터를 조회하고, Kibana에서 시각화하여 실시간 확인할 수 있습니다.

## ✨ 주요 기능

✅ 고객 번호 입력 후 Elasticsearch에서 데이터 검색 및 Kibana 시각화 제공✅ Flask 기반 웹 애플리케이션, Kibana 연동✅ Filebeat & Logstash를 이용한 실시간 데이터 수집✅ Kibana 대시보드 필터 적용을 통한 동적 데이터 조회

## 🛠 기술 스택

Backend: Flask, Python 🐍

Frontend: HTML, Jinja2, Bootstrap 🎨

Database & Search Engine: Elasticsearch 🔎

Log Processing: Logstash, Filebeat 📊

Visualization: Kibana 📈

## 📥 설치 방법

### 1️⃣ 프로젝트 클론

$ git clone https://github.com/YOUR_USERNAME/flask-kibana-dashboard.git
$ cd flask-kibana-dashboard

### 2️⃣ 가상환경 설정 및 패키지 설치

$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate
$ pip install -r requirements.txt

### 3️⃣ 환경 변수 설정

.env 파일을 생성하고 다음과 같이 설정합니다.

KIBANA_URL=https://YOUR_KIBANA_URL
ELASTICSEARCH_HOST=http://localhost:9200
SECRET_KEY=your_secret_key

### 4️⃣ 애플리케이션 실행

$ flask run --host=0.0.0.0 --port=5000

## 📌 사용법

1️⃣ 브라우저에서 http://localhost:5000 접속2️⃣ 고객 번호 입력 후 데이터 조회3️⃣ Kibana 대시보드에서 실시간 데이터 확인 가능

❗ 트러블슈팅

### 🔹 1. "Flask 세션 유지 안됨" 문제 발생

문제: 사용자가 로그인했으나 페이지 이동 후 세션이 유지되지 않음해결 방법:

.env 파일에서 SECRET_KEY가 설정되었는지 확인.

app.py에서 Flask 세션 구성 확인:

from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

### 🔹 2. "Kibana iframe이 로드되지 않음" 문제 발생

문제: Kibana에서 보안 정책으로 인해 iframe 내에서 로드되지 않음해결 방법:

kibana.yml 설정 파일에서 xpack.security.sameSiteCookies: None 추가.

Content-Security-Policy 헤더를 적절히 조정하여 frame-ancestors를 허용.

$ echo 'kibana.security.disableEmbedding: true' >> /etc/kibana/kibana.yml

변경 후 Kibana를 재시작:

$ systemctl restart kibana

### 🔹 3. "Filebeat 데이터가 Elasticsearch에 반영되지 않음"

문제: Filebeat가 로그를 수집하고 있지만 Elasticsearch에서 데이터가 검색되지 않음해결 방법:

Filebeat 설정 확인:

$ cat /etc/filebeat/filebeat.yml

output.elasticsearch 부분이 올바르게 설정되었는지 확인.

Filebeat 서비스 상태 확인:

$ systemctl status filebeat

Filebeat 재시작:

$ systemctl restart filebeat

## 💡 기여 방법

1️⃣ 이 저장소를 포크합니다.2️⃣ 새로운 브랜치를 생성합니다 (git checkout -b feature-branch).3️⃣ 변경 사항을 커밋합니다 (git commit -m 'Add new feature').4️⃣ 브랜치에 푸시합니다 (git push origin feature-branch).5️⃣ Pull Request를 생성합니다.

## 📜 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 📝

