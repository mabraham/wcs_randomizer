from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import json
import random
from randomizer.models import SpotlightDancer

class AllSkateView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'All-skate display'}
        return render(request, 'allskate.html', context)

class AllSkateMCView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'All-skate MC'}
        return render(request, 'allskate_mc.html')

class SpotlightView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'Spotlight display'}
        return render(request, 'spotlight.html', context)

class SpotlightMCView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'Spotlight MC'}
        return render(request, 'spotlight_mc.html')

class SpotlightDancerView(View):

    def get(self, request, *args, **kwargs):
        spotlight_dancers_who_have_not_danced = SpotlightDancer.objects.filter(has_danced__exact=False)
        number_of_dancers_remaining = len(spotlight_dancers_who_have_not_danced)
        if number_of_dancers_remaining > 0:
            bib_number = random.choice(spotlight_dancers_who_have_not_danced).bib_number
            choice = str(bib_number)

            # Now set the flag to show that this one has danced
            that_dancer_set = SpotlightDancer.objects.filter(bib_number__exact=bib_number)
            that_dancer = that_dancer_set[0]
            that_dancer.has_danced = True
            that_dancer.save()

        else:
            that_dancer = SpotlightDancer(name="", bib_number="   ", has_danced=False, id="")

        dict_obj = model_to_dict(that_dancer)
        response = JsonResponse(dict_obj, safe=False)

        return response

class SpotlightResetView(View):

    def get(self, request):
        spotlight_dancers = SpotlightDancer.objects.all()
        spotlight_dancers.update(has_danced=False)
        for item in spotlight_dancers:
            item.save()
        
        return HttpResponse("OK")
