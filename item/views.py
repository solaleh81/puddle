from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import NewItemForm


from .models import Category, Item


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=id
    )[0:3]

    return render(
        request,
        "item/item_detail.html",
        context={
            "item": item,
            "category": item.category,
            "related_items": related_items,
        },
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", id=item.id)
    else:
        form = NewItemForm()

    return render(request, "item/form.html", context={"form": form})
