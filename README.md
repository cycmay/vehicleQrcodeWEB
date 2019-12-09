## Vehiclebrand Web

## 简介：

使用Django + Gunicorn + Nginx + Docker +Supervisor搭建的旅游包车车牌系统。

##  How to install:

1. Git clone this respority on your local dir.
2. 在项目根目录创建 `/.envs/.production` 表示Django 框架提供的SECRET KEY，文件内容如下：
   `DJANGO_SECRET_KEY=your key`
3. 安装Python3.7 docker-compose，并添加软连接
4. 安装并启动适应你系统的Docker
5. 在项目根目录，命令行输入: `$docker-compose -f production.yml up --build` 表示启动生产环境；输入：`docker-compose -f local.yml up --build` 表示启动Django自带服务器环境。
6. supervisor使用以及其他依赖安装方法见详细[部署文件](https://github.com/cycmay/notes/blob/master/Docker/Docker_compose.md)。

##  √ Tips:

1. 项目根目录下收集完静态文件后生成 /static 目录，要手动创建一个media文件夹，保存项目生成的二维码图片，在start.sh 中写入了shell脚本，自动生成该目录。在本地开发环境中，为了使Django服务器识别media目录，在配置文件common.py中写入：

   ```python
   STATICFILES_DIRS = (
       ('media', os.path.join(STATIC_ROOT, 'media').replace('\\', '/')),
   )
   ```

   

2. 为了区分本地开发环境配置与生产服务器配置，该项目设置了compose/local 和 compose/production

## ∑ TODO:





### 