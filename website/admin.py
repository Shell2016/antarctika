from django.contrib import admin
from django.forms import TextInput, Textarea

from .models import Promo, PromoItem


class PromoItemInline(admin.StackedInline):
    model = PromoItem
    extra = 0


class PromoAdmin(admin.ModelAdmin):
    fields = ['title', 'content_title',
              'content_text', 'footer_text']
    inlines = [PromoItemInline]


admin.site.register(Promo, PromoAdmin)
