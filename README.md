### 富文本编辑器

- pip install django-ckeditor
- ckeditor.fields.RichTextField 不支持上传文件的富文本字段
  ckeditor_uploader.fields.RichTextUploadingField 支持上传文件的富文本字段

- sitting.py 注册，配置
```python
    INSTALLED_APPS = [
    ...
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    ...
]
```
```python
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''
```
- 路由
```python
url(r'^ckeditor/', include('ckeditor_uploader.urls')),
```
### redis 数据库分配
- 连接redis redis-cli -h 127.0.0.1(如果是默认端口号就不用写)
    - 数据库选择 select 0
    - 查看数据库 keys *
    
- 0号 caches
- 1号 session
- 2号 celery


### celery 异步发邮件

- pip install celery
- 配置settings
    ```python
        '''发送邮件配置'''
        EMAIL_HOST = 'smtp.126.com'
        EMAIL_PORT = 25
        EMAIL_HOST_USER = 'haijun0427@126.com'
        EMAIL_HOST_PASSWORD = 'xy0407'
        EMAIL_USE_TLS = True
        EMAIL_FROM = 'haijun0427@126.com'
    ```

- 启动 
    ```python
    celery -A celery_task.tasks worker -l info
    ```
- 发送邮件报错
    ```python
    新注册邮箱会报错 smtplib.SMTPAuthenticationError: (535, b'Error: authentication failed'),可以用授权码代替密码
    ``` 
    
### FastDFS

