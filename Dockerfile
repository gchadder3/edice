FROM python:3-alpine

WORKDIR /app

COPY edice.py .

CMD ["python", "edice.py"]
