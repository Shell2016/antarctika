from django.shortcuts import render
# from django.views.generic.base import TemplateView

from .models import Promo


# class PromoTemplateView(TemplateView):
#     model = Promo
#     template_name = 'website/promo.html'


def promo(request):
    promo = Promo.objects.all().first()
    context = {'promo': promo}
    return render(request, 'website/promo.html', context)
