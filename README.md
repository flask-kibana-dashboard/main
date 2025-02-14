# Flask-Kibana Dashboard


## ✅ 프로젝트 개요
Flask와 ELK(Stack)인 Elasticsearch, Logstash, Kibana, Filebeat를 활용하여 실시간 고객 데이터를 조회할 수 있는 대시보드 애플리케이션입니다. 사용자가 고객 번호를 입력하면 해당 데이터를 조회하고, Kibana에서 시각화하여 실시간으로 확인할 수 있습니다.



## ✅ 주요 기능
고객 번호를 입력하면 Elasticsearch에서 데이터를 검색 후 시각화된 대시보드를 제공

Flask 기반의 웹 애플리케이션으로 Kibana와 연동

Filebeat 및 Logstash를 이용한 실시간 데이터 수집 및 전송

Kibana 대시보드 필터 적용을 통한 동적 데이터 조회



## ✅ Tools - 기술 스택
Backend: Flask, Python

Frontend: HTML, Jinja2, Bootstrap

Database & Search Engine: Elasticsearch

Log Processing: Logstash, Filebeat

Visualization: Kibana


## ❗❗ 트러블슈팅
### 1. "Flask 세션 유지 안됨" 문제 발생

문제:

사용자가 로그인했으나 페이지 이동 후 세션이 유지되지 않음.

해결 방법:

.env 파일에서 SECRET_KEY가 설정되었는지 확인.

app.py에서 Flask 세션 구성 확인:

from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)



### 2. "Kibana iframe이 로드되지 않음" 문제 발생

문제:

Kibana에서 보안 정책으로 인해 iframe 내에서 로드되지 않음.

해결 방법:

kibana.yml 설정 파일에서 xpack.security.sameSiteCookies: None 추가.

Content-Security-Policy 헤더를 적절히 조정하여 frame-ancestors를 허용.

$ echo 'kibana.security.disableEmbedding: true' >> /etc/kibana/kibana.yml

변경 후 Kibana를 재시작:

$ systemctl restart kibana

3. "Filebeat 데이터가 Elasticsearch에 반영되지 않음"

문제:

Filebeat가 로그를 수집하고 있지만 Elasticsearch에서 데이터가 검색되지 않음.

해결 방법:

Filebeat 설정 확인:

$ cat /etc/filebeat/filebeat.yml

output.elasticsearch 부분이 올바르게 설정되었는지 확인.

Filebeat 서비스 상태 확인:

$ systemctl status filebeat

Filebeat 재시작:

$ systemctl restart filebeat




## ✅ 느낀점
- 로컬 환경에서 제작한 대시보드를 다른 컴퓨터에서 열람하게 하는 데 어려움이 있었음.
- 데이터량이 많아 전처리를 하는 데에도 다소 어려움이 존재 (ex.타임아웃 발생 등..)