FROM python:3.8-slim
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR ${APP_HOME}

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]