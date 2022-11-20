from django.shortcuts import render

# Create your views here.

def calendar(request):
    return render(request,'calendarapp/base.html', context={'context_variable': 'value'})
    