# 🚀 Flask-Kibana Dashboard

---

## 📌 프로젝트 개요
Flask와 ELK(Stack)인 **Elasticsearch, Logstash, Kibana, Filebeat**를 활용하여 **실시간 고객 데이터를 조회**할 수 있는 대시보드 애플리케이션입니다. 사용자가 고객 번호를 입력하면 해당 데이터를 조회하고, Kibana에서 **시각화하여 실시간 확인**할 수 있습니다.

---

## ✨ 주요 기능
✅ 고객 번호 입력 후 **Elasticsearch에서 데이터 검색 및 Kibana 시각화 제공**  
✅ **Flask** 기반 웹 애플리케이션, **Kibana** 연동  
✅ **Filebeat & Logstash**를 이용한 실시간 데이터 수집  
✅ **Kibana 대시보드 필터 적용**을 통한 동적 데이터 조회

---

## 🛠 기술 스택
- **Backend** : ![Python](https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000.svg?&style=for-the-badge&logo=flask&logoColor=white)

 
- **Frontend** : ![Html5](https://img.shields.io/badge/html5-E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)

  
- **Database & Search Engine** : ![Elasticsearch](https://img.shields.io/badge/elasticsearch-005571.svg?&style=for-the-badge&logo=elasticsearch&logoColor=white)

- **Visualization** : ![Kibana](https://img.shields.io/badge/kibana-005571.svg?&style=for-the-badge&logo=kibana&logoColor=white)

---

## ❗ 트러블슈팅

🛑 문제 1. Elasticsearch 연결 오류 (elasticsearch.exceptions.ConnectionError)

    💬 원인:

        Config.ELASTICSEARCH_URL 설정 오류
        Elasticsearch 실행되지 않음 또는 다른 포트에서 실행 중
        방화벽 또는 보안 그룹에서 연결 차단

    ✅ 해결 방법:

        sudo systemctl status elasticsearch  # Elasticsearch 실행 여부 확인
        
        docker ps  # Docker에서 실행 중인지 확인
        
        실행 중인 포트 확인 후 적절히 수정

🛑 문제 2 : 로그인 실패 (고객번호 SEQ 조회 불가)

    💬 원인:

        SEQ 필드가 존재하지 않음
        match 쿼리 사용으로 정확한 검색 불가 (keyword 타입 문제)
        인덱스에 데이터가 없음

    ✅ 해결 방법:
        
        결과가 비어 있거나 SEQ 필드 없음 → 데이터 삽입 필요
        
        match 대신 term 사용하여 정확한 검색
        
        body = {
            "query": {
                "term": {
                    "SEQ.keyword": seq  # 정확한 일치 검색
                }
            }
        }


🛑 문제 3 : iframe에서 Kibana 대시보드가 로딩되지 않음

   💬 원인:

       Kibana 보안 설정으로 iframe 로딩 차단됨
       URL 필터가 올바르게 적용되지 않음

   ✅ 해결 방법:

       Kibana 설정 변경 (kibana.yml)
       
       server.publicBaseUrl: "http://localhost:5601"
       xpack.security.sameSiteCookies: None
       
       iframe 로딩을 허용하기 위해 설정 변경


---

## 🎞 실행화면

<img src="https://github.com/user-attachments/assets/87a66efe-df4f-47f6-a559-029ed1a67d7d">


---

## 📥 실행 방법
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


### 3️⃣ 애플리케이션 실행
```sh
$ python app.py
```

---

## 📌 사용법
1️⃣ 브라우저에서 `http://localhost:5000` 접속  
2️⃣ 고객 번호 입력 후 데이터 조회  
3️⃣ Kibana 대시보드에서 **실시간 데이터 확인 가능**  

