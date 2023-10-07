from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('printPDF',views.CreatePDF,name="printPDF"),
    path('المطالب',views.requests,name="requests"),
    path('مطلب-حجز-قاعة',views.demandeDeSalle,name="demande-de-salle"),



]