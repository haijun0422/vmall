from django.shortcuts import render, render_to_response
from django.views.generic import View, ListView
from users.models import User
from .models import GoodsCategory


# Create your views here.
class IndexView(View):
    def get(self, request):
        user = request.user
        category_parents = GoodsCategory.objects.filter(parent_id=0).order_by('sort')  # 获取一级类
        first_category_list = []  # 构建多维数组传给前端
        for category_parent in category_parents:
            category_children = GoodsCategory.objects.filter(parent_id=category_parent.id)  # 获取对应的二级类
            second_category_list = []
            for category in category_children:
                cate_children = GoodsCategory.objects.filter(parent_id=category.id)  # 获取对应的三级类
                third_category_list = []
                for c in cate_children:
                    third_category_list.append(c.name)
                second_category_list.append((category.name, third_category_list))  # 元组
            first_category_list.append((category_parent.name, second_category_list))  # 元组
        content = {
            'user': user,
            'cat_list': first_category_list,
        }
        return render_to_response('index.html', content)
