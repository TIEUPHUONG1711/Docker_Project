# Chọn base image Python nhẹ
FROM python:3.11-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy requirements và cài package
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ project
COPY . .

# Expose port 5000
EXPOSE 5000

# Chạy Flask app
CMD ["python", "run.py"]
