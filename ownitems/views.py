from django.shortcuts import render
from django.http import HttpResponse
from .models import CategoryItem, Item

# Create your views here.

def category_view(request):
    l = CategoryItem.objects.all()
    item = Item.objects.all()
    context = {"category": l,
               "item": item}
    return render(request, template_name="view.html", context=context)