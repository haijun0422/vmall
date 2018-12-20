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
