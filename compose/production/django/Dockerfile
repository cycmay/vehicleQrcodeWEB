FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# 设置清华源apk
RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

RUN apk update \
  # Pillow dependencies
 && apk add g++ jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /app

RUN pip install pipenv -i https://pypi.douban.com/simple

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app

COPY ./compose/production/django/start.sh /start.sh

RUN chmod +x /start.sh