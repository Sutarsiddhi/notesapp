from django.contrib import admin
from django.urls import path
from notesapp.views import home,create,edit,delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("create",create,name="create"),
    path("edit/<int:id>",edit,name="edit"),
    path("delete/<int:id>",delete,name="delete"),
]
