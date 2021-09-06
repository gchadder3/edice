FROM continuumio/anaconda3

WORKDIR /app

COPY edice.py .

CMD ["python", "edice.py"]
