from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User


from .models import Category, Item

def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=id)[0:3]

    return render (request, 'item/item_detail.html', context={'item': item, 'category': item.category, 'related_items': related_items})
