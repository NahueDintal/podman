FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY counter-app/app.py .
ENV FLASK_ENV=development
CMD ["python", "app.py"]
