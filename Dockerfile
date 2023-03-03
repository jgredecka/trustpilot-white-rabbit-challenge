FROM python:3.9

WORKDIR /app

COPY . /app

CMD ["python", "phrase_finder.py"]