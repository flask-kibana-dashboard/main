function updateCustomerInfo() {
    fetch('/customer_data')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                window.location.href = '/';  // 로그인 페이지로 리다이렉트
            } else {
                document.getElementById('customer-info').innerHTML = `
                    <p>고객 번호: ${data.customer_id}</p>
                    <p>이름: ${data.name}</p>
                    <p>나이: ${data.age}</p>
                    <p>위치: ${data.location}</p>
                `;
            }
        });
}

// 5초마다 고객 정보 업데이트
setInterval(updateCustomerInfo, 5000);
