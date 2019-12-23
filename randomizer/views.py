from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class DisplayView(View):
#    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {'title': 'All-skate randomizer'}
        return render(request, 'display.html', context)

class MCView(View):
#    template_name = "index.html"

    def get(self, request, *args, **kwargs):
#        context = {'title': 'Display'}
        return render(request, 'mc.html')
