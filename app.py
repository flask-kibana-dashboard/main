from flask import Flask, render_template, request, redirect, url_for, session
from elasticsearch import Elasticsearch
import logging
from config import Config

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

# Elasticsearch 연결
es = Elasticsearch(Config.ELASTICSEARCH_URL)

# 로깅 설정
logging.basicConfig(filename='logs/flask_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        seq = request.form.get('seq')

        # Elasticsearch에서 SEQ 기준 검색
        body = {
            "query": {
                "match": {
                    "SEQ": seq
                }
            }
        }
        result = es.search(index="edu-data", body=body)

        if result['hits']['total']['value'] > 0:
            session['seq'] = seq
            logging.info(f"User SEQ {seq} logged in.")
            return redirect(url_for('dashboard'))
        else:
            logging.warning(f"Failed login attempt for SEQ: {seq}")
            return "해당 SEQ를 가진 고객 정보를 찾을 수 없습니다."

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'seq' not in session:
        return redirect(url_for('login'))

    seq = session['seq']
    logging.info(f"User SEQ {seq} accessed the dashboard.")

    # Kibana 대시보드 필터링 URL
    kibana_dashboard_url = f"{Config.KIBANA_URL}/app/dashboards#/view/YOUR_DASHBOARD_ID?_g=(filters:!((query:(match_phrase:(SEQ:'{seq}')))))"

    return render_template('dashboard.html', kibana_dashboard_url=kibana_dashboard_url)

if __name__ == '__main__':
    app.run(debug=True)
