FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY app /app

VOLUME ["/app/static/memes"]

EXPOSE 5000

CMD ["python", "main.py"]
