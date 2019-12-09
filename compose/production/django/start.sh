#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
# media目录保存项目生成的图片
dir="./static/media"
if [ ! -d "$dir" ];then
mkdir -p $dir
echo "created ./static/media !"
else
echo "./static/media already exsited!"
fi
gunicorn vehicleBrand.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app