# Flask-Kibana Dashboard

## 프로젝트 개요

Flask와 ELK(Stack)인 Elasticsearch, Logstash, Kibana, Filebeat를 활용하여 실시간 고객 데이터를 조회할 수 있는 대시보드 애플리케이션입니다. 사용자가 고객 번호를 입력하면 해당 데이터를 조회하고, Kibana에서 시각화하여 실시간으로 확인할 수 있습니다.

## 주요 기능

고객 번호를 입력하면 Elasticsearch에서 데이터를 검색 후 시각화된 대시보드를 제공

Flask 기반의 웹 애플리케이션으로 Kibana와 연동

Filebeat 및 Logstash를 이용한 실시간 데이터 수집 및 전송

Kibana 대시보드 필터 적용을 통한 동적 데이터 조회

## ✅Tools - 기술 스택

Backend: Flask, Python

Frontend: HTML, Jinja2, Bootstrap

Database & Search Engine: Elasticsearch

Log Processing: Logstash, Filebeat

Visualization: Kibana
