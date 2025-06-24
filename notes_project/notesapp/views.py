from django.shortcuts import render, redirect, get_object_or_404
from .models import NoteModel
from .forms import NoteForm

def home(request):
    data = NoteModel.objects.all().order_by("-dt")
    return render(request, "home.html", {"data": data})

def create(request):
    if request.method == "POST":
        data = NoteForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home")
        else:
            msg = "issue"
            return render(request, "create.html", {"fm": data, "msg": msg})
    else:
        fm = NoteForm()
        return render(request, "create.html", {"fm": fm})

def edit(request, id):
    d = NoteModel.objects.get(id=id)
    if request.method == "POST":
        data = NoteForm(request.POST, instance=d)
        if data.is_valid():
            data.save()
            return redirect("home")
        else:
            msg = "Check issue"
            return render(request, "edit.html", {"fm": data})
    else:
        fm = NoteForm(instance=d)
        return render(request, "edit.html", {"fm": fm})

def delete(request, id):
    # Fetch the note object or return a 404 error if not found
    note = get_object_or_404(NoteModel, id=id)
    # Delete the note
    note.delete()
    # Redirect to the home page after deletion
    return redirect("home")