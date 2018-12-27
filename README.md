
### 富文本编辑器
- pip install django-ckeditor
### redis 数据库分配
- 0号 caches
- 1号 session
- 2号 celery
### celery 异步发邮件
- pip install celery
- 发送邮件报错
    ```python
    新注册邮箱会报错 smtplib.SMTPAuthenticationError: (535, b'Error: authentication failed'),可以用授权码代替密码
    ```     
### FastDFS
- 安装fastdfs依赖包libfastcommon-master.zip

- 安装fastdfs
        wget https://github.com/happyfish100/fastdfs/archive/V5.11.tar.gz 
- 配置跟踪服务器tracker
 
- 配置存储服务器storage

- 测试是否安装成功
    如果返回类似group1/M00/00/00/rBIK6VcaP0aARXXvAAHrUgHEviQ394.jpg的文件id则说明文件上传成功

- 安装nginx及fastdfs-nginx-module