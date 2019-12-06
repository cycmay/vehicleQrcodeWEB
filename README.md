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
6. supervisor使用以及其他依赖安装方法见详细部署文件。

 





### 