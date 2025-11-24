# Docker_Project
# QuoteApp Docker

## Mô tả
Ứng dụng Flask đơn giản trả về **Quote of the Day**.  
Chạy trong Docker, dễ deploy trên bất kỳ máy nào có Docker.
# Cách chạy:
- Kiểm tra Docker version:
docker --version
- Bước 1: Clone repository
git clone https://github.com/TIEUPHUONG1711/Docker_Project.git
cd Docker_Project

- Bước 2: Xây dựng Docker image
 docker build -t docker_flask_app .

- Bước 3: Chạy container
 docker run -p 5000:5000 docker_flask_app


- Bước 4: Truy cập ứng dụng qua:
 http://localhost:5000

- Rebuild (nếu bạn thay đổi code)
- rebuild the image:
docker build -t docker_flask_app .
docker run -p 5000:5000 docker_flask_app

- Nếu muốn dừng hay xóa container:
- Liệt kê containers đang chạy:
docker ps
- Dừng container:
docker stop <container_id>
* container_id lấy từ lệnh docker ps
- Xóa container:
docker rm <container_id>


Remove image (optional):

docker rmi docker_flask_app

## Cấu trúc project:
Docker_Project/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md


