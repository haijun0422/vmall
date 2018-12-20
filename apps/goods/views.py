from django.shortcuts import render
from django.views.generic import View
from users.models import User


# Create your views here.
class IndexView(View):
    def get(self, request):
        user = request.user
        content = {
            'user': user,
        }
        return render(request, 'index.html', content)
