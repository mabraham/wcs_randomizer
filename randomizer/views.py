from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class DisplayView(View):
#    template_name = "index.html"

    def get(self, request, *args, **kwargs):
#        return HttpResponse('Hello, World!')
        return render(request, 'index.html')
