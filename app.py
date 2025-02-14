import csv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"  # 세션 관리용

# 🔹 CSV 파일에서 고객 데이터를 불러오는 함수
def load_customer_data():
    customer_dict = {}
    with open("customer_data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer_dict[row["customer_id"]] = row  # 고객 ID를 키로 저장
    return customer_dict

# 🔹 1️⃣ 로그인 페이지
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        customer_data = load_customer_data()  # CSV에서 데이터 로드
        if customer_id in customer_data:
            session["customer"] = customer_data[customer_id]
            return redirect(url_for("dashboard"))
        return "잘못된 고객 번호입니다!", 400
    return render_template("login.html")

# 🔹 2️⃣ 대시보드 페이지
@app.route("/dashboard")
def dashboard():
    if "customer" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", customer=session["customer"])

# 🔹 3️⃣ AJAX 요청을 처리하는 API (실시간 고객 정보 업데이트)
@app.route("/customer_data")
def customer_data():
    if "customer" in session:
        return jsonify(session["customer"])
    return jsonify({"error": "로그인이 필요합니다."}), 403

if __name__ == "__main__":
    app.run(debug=True)
