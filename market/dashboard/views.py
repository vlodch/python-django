from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items': items,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk, created_by=request.user)
    item.delete()