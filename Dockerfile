FROM python:3.11-slim

WORKDIR /app

COPY src/requirement.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

ENV APP_VERSION=unknown
ENV APP_ENV=unknown

CMD ["python", "app.py"]