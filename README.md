# 🚀 Flask-Kibana Dashboard

---

## 📌 프로젝트 개요
Flask와 ELK(Stack)인 **Elasticsearch, Logstash, Kibana, Filebeat**를 활용하여 **실시간 고객 데이터를 조회**할 수 있는 대시보드 애플리케이션입니다. 사용자가 고객 번호를 입력하면 해당 데이터를 조회하고, Kibana에서 **시각화하여 실시간 확인**할 수 있습니다.

---

## ✨ 주요 기능
✅ 고객 번호 입력 후 **Elasticsearch에서 데이터 검색 및 Kibana 시각화 제공**  
✅ **Flask 기반 웹 애플리케이션**, Kibana 연동  
✅ **Filebeat & Logstash를 이용한 실시간 데이터 수집**  
✅ **Kibana 대시보드 필터 적용을 통한 동적 데이터 조회**  

---

## 🛠 기술 스택
- **Backend**: Flask, Python 🐍
- **Frontend**: HTML 🎨
- **Database & Search Engine**: Elasticsearch 🔎
- **Visualization**: Kibana 📈

---

## 📥 설치 방법
### 1️⃣ 프로젝트 클론
```sh
$ git clone https://github.com/YOUR_USERNAME/flask-kibana-dashboard.git
$ cd flask-kibana-dashboard
```

### 2️⃣ 가상환경 설정 및 패키지 설치
```sh
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```

### 3️⃣ 환경 변수 설정
`config.py` 파일을 생성하고 다음과 같이 설정합니다.
```ini
    SECRET_KEY = "your_secret_key"
    INDEX = "your_index_name"
    ELASTICSEARCH_URL = "http://localhost:9200"
    KIBANA_URL = "http://localhost:5601"
    DASHBOARD_ID = "your_dashboard_id"

```

### 4️⃣ 애플리케이션 실행
```sh
$ flask run --host=0.0.0.0 --port=5000
```

---

## 📌 사용법
1️⃣ 브라우저에서 `http://localhost:5000` 접속  
2️⃣ 고객 번호 입력 후 데이터 조회  
3️⃣ Kibana 대시보드에서 **실시간 데이터 확인 가능**  

---

## ❗ 트러블슈팅
1. Elasticsearch 연결 오류

🛑 문제: elasticsearch.exceptions.ConnectionError 발생

💬 원인:

Config.ELASTICSEARCH_URL 설정 오류

Elasticsearch 실행되지 않음 또는 다른 포트에서 실행 중

방화벽 또는 보안 그룹에서 연결 차단

✅ 해결 방법:

Elasticsearch 상태 확인

curl -X GET "http://localhost:9200/_cluster/health?pretty"

응답이 없거나 yellow 또는 red 상태라면 비정상 상태

Elasticsearch 실행 여부 확인

sudo systemctl status elasticsearch  # Linux

docker ps  # Docker에서 실행 중인지 확인

Flask 설정 (config.py) 수정

ELASTICSEARCH_URL = "http://localhost:9200"

실행 중인 포트 확인 후 적절히 수정

2. 로그인 실패 (고객번호 SEQ 조회 불가)

🛑 문제: Elasticsearch에서 SEQ 값을 찾을 수 없음

💬 원인:

SEQ 필드가 존재하지 않음

match 쿼리 사용으로 정확한 검색 불가 (keyword 타입 문제)

인덱스에 데이터가 없음

✅ 해결 방법:

Elasticsearch 인덱스 확인

curl -X GET "http://localhost:9200/edu-data/_search?pretty"

결과가 비어 있거나 SEQ 필드 없음 → 데이터 삽입 필요

match 대신 term 사용하여 정확한 검색

body = {
    "query": {
        "term": {
            "SEQ.keyword": seq  # 정확한 일치 검색
        }
    }
}

인덱스 존재 여부 확인

curl -X GET "http://localhost:9200/_cat/indices?v"

edu-data 인덱스가 없으면 데이터를 다시 삽입

3. Kibana 대시보드가 정상적으로 표시되지 않음

🛑 문제: iframe에서 Kibana 대시보드가 로딩되지 않음

💬 원인:

Kibana 보안 설정으로 iframe 로딩 차단됨

URL 필터가 올바르게 적용되지 않음

✅ 해결 방법:

Kibana 설정 변경 (kibana.yml)

server.publicBaseUrl: "http://localhost:5601"
xpack.security.sameSiteCookies: None

iframe 로딩을 허용하기 위해 설정 변경

SEQ 필터 정상 동작 확인

http://localhost:5601/app/dashboards#/view/YOUR_DASHBOARD_ID?_g=(filters:!((query:(match_phrase:(SEQ:'1001')))))

SEQ 값이 정상적으로 전달되는지 확인



---

## 💡 기여 방법
1️⃣ 이 저장소를 **포크**합니다.  
2️⃣ 새로운 브랜치를 생성합니다 (`git checkout -b feature-branch`).  
3️⃣ 변경 사항을 커밋합니다 (`git commit -m 'Add new feature'`).  
4️⃣ 브랜치에 푸시합니다 (`git push origin feature-branch`).  
5️⃣ **Pull Request**를 생성합니다.  

---

## 📜 라이선스
이 프로젝트는 **MIT 라이선스**를 따릅니다. 📝

