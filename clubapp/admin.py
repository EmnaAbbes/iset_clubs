from django.contrib import admin
from .models import مطلب_حجز_قاعة
from .models import  مطلب_نشاط
from .models import بيانات_النادي
# Register your models here.
admin.site.register( مطلب_حجز_قاعة)
admin.site.register(مطلب_نشاط)
admin.site.register(بيانات_النادي)