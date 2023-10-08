from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('printPDF',views.CreatePDF,name="printPDF"),
    path('المطالب',views.requests,name="requests"),
    path('مطلب-حجز-قاعة',views.demandeDeSalle,name="demande-de-salle"),
    path('مطلب_نشاط',views.demandeEvenement,name="demande-evenement"),
    path('مطالب-حجز-القاعات/<int:id>',views.DemmSalle,name="disDemmSalle"),
    path('مطالب-الأنشطة/<int:id>',views.DemmEven,name="disDemmEven"),
    path('list-des-clubs',views.clubsView,name="disClubs"),
    path('list-des-demandes/<int:id>',views.ListDemmandes,name="ListDemandes"),



]