from django.shortcuts import render
from django.views.generic import View
from authentication.models import User
# Create your views here.


class BaseView(View):
    def get(self, request, *args, **kwargs):
        pass
        return render(request, 'base.html')