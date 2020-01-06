import random
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from randomizer.models import SpotlightDancer

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

class SpotlightView(View):

    def get(self, request, *args, **kwargs):
        context = {'title': 'Spotlight randomizer'}
        return render(request, 'spotlight.html', context)

class SpotlightDancerView(View):

    def get(self, request, *args, **kwargs):
        spotlight_dancers_who_have_not_danced = SpotlightDancer.objects.filter(has_danced__exact=False)
        number_of_dancers_remaining = len(spotlight_dancers_who_have_not_danced)
        choice = ''
        if number_of_dancers_remaining > 0:
            bib_number = random.choice(spotlight_dancers_who_have_not_danced).bib_number
            choice = str(bib_number)

            # Now set the flag to show that this one has danced
            that_dancer = SpotlightDancer.objects.get(bib_number__exact=bib_number)
            that_dancer.has_danced = True
            that_dancer.save()

        return JsonResponse(choice, safe=False)

class SpotlightMCView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'spotlight_mc.html')

class SpotlightResetView(View):

    def get(self, request):
        spotlight_dancers = SpotlightDancer.objects.all()
        spotlight_dancers.update(has_danced=False)
        for item in spotlight_dancers:
            item.save()
        
        return HttpResponse("OK")
