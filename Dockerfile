FROM python:3.10-slim

WORKDIR /app/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "converter.py"]
