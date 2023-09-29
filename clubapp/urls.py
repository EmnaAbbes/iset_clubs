from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('pdf',views.CreatePDF,name="pdf"),
    path('htmlpage',views.htmlpage,name="html")


]