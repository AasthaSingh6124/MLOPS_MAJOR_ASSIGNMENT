FROM python:3.11-slim

WORKDIR /app

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy code and saved model
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
