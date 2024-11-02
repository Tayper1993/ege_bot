FROM python:alpine
LABEL version="0.1.0" maintainer="Polyakov_KS"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG ru_RU.UTF-8

WORKDIR /telegram_bot_ege

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./ ./

RUN chmod -R 777 ./

CMD ["python", "./main.py"]
