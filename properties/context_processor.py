from . models import Category
from . choices import * 


def category(request):
    category = Category.objects.all()
    context = {
        'categorys':category
    }
    return context

def searchLists(request):
    context = {
        'bedroom_choices':bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'garage_choices':garage_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
    }
    return context
