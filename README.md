## Docker_Project
## Quote of the day

## Mô tả Ứng dụng Flask đơn giản trả về **Quote of the Day**. Chạy trong Docker, dễ deploy trên bất kỳ máy nào có Docker.

📦 Cách chạy dự án
1️⃣ Kiểm tra Docker
docker --version

2️⃣ Clone repository
git clone https://github.com/TIEUPHUONG1711/Docker_Project.git
cd Docker_Project

3️⃣ Build Docker image
docker build -t docker_flask_app .

4️⃣ Chạy container
docker run -p 5000:5000 docker_flask_app


Truy cập ứng dụng tại:
👉 http://localhost:5000

🔁 Rebuild khi cập nhật code

Nếu bạn thay đổi nội dung project, hãy build lại image:

- docker build -t docker_flask_app .
- docker run -p 5000:5000 docker_flask_app

🛑 Dừng & Xóa container
Liệt kê container đang chạy:
docker ps

Dừng container:
docker stop <container_id>

* container_id lấy từ cột CONTAINER ID trong docker ps.

Xóa container:
docker rm <container_id>

Xóa image (tùy chọn):
docker rmi docker_flask_app

📁 Cấu trúc dự án
Docker_Project/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
