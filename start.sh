#!/bin/sh
dir="./static/media"
if [ ! -d "$dir" ];then
mkdir -p $dir
echo "created ./static/media !"
else
echo "./static/media already exsited!"
fi

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
