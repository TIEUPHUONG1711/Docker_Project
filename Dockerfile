# Chọn base image Python nhẹ
FROM python:3.11-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy requirements và cài package
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app ./app

# Expose port 5000
EXPOSE 5000

# Chạy Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
