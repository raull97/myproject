from django.shortcuts import render, redirect
from django.contrib import messages
from forms import TodoForm
from models import Todo


def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POTS)
        if form.is_valid():
            form.save()
            return redirect("Todo")
        form = TodoForm()

        page = {

            "forms": form,
            "list": item_list,
            "title": "TODO",
        }

        return render(request, 'Todo/index.html', page)

        def remove(request, item_id):
            item = Todo.objects.get(id=item_id)
            item = delete()
            messages.info(request, "item removed !!!")
            return redirect('Todo')
