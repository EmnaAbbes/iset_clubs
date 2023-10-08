from django.db import models
class بيانات_النادي(models.Model):
    CHOICES = (
        ('نادي_عام','نادي_عام'),
        ('نادي_خاص','نادي_خاص')
    )
    نوع_النادي=models.CharField(max_length=255,choices=CHOICES)
    اسم_النادي=models.CharField(max_length=255)
    تخصص_النادي=models.CharField(max_length=1000)
    فكرة_النادي=models.CharField(max_length=1000)
    رسالة_النادي=models.CharField(max_length=1000)
    رؤية_النادي=models.CharField(max_length=1000)
    أهداف_النادي=models.CharField(max_length=1000)  
    الطلبة= models.BooleanField(default=False)
    الشركات= models.BooleanField(default=False)
    المنشآت_العمومية=models.BooleanField(default=False)
    الطلبة_من_خارج_المؤسسة= models.BooleanField(default=False)
    الصّناعيين=models.BooleanField(default=False)
    الدواوين=models.BooleanField(default=False)
    def __str__(self):
        return self.اسم_النادي
class مطلب_حجز_قاعة(models.Model):
    CHOICES = (
        ('قاعة ملتقيات الإدارة', 'قاعة ملتقيات الإدارة'),
        ('قاعة ملتقيات الطلبة', 'قاعة ملتقيات الطلبة'),
        ('قاعة 4', 'قاعة 4'),
        ('قاعة قسم', 'قاعة قسم'),
        ('المكتبة', 'المكتبة'),
        ('Amphi', 'Amphi'),
        ('Amphi Théâtre', 'Amphi Théâtre'),
    )
    
    القاعة= models.CharField(max_length=255, choices=CHOICES)
    اسم_النادي_أو_المنظمة = models.ForeignKey(بيانات_النادي, on_delete=models.CASCADE,null=True)
    اسم_و_لقب_رئيس_النادي_أو_المنظمة = models.CharField(max_length=255)
    الموضوع = models.CharField(max_length=1000)
    اليوم_و_التوقيت = models.DateTimeField()
    ادارة_النشاط_الثقافي = models.CharField(max_length=255)
    اسم_الاستاذ_المشرف = models.CharField(max_length=255)
    رقم_الهاتف = models.CharField(max_length=8)
    def __str__(self):
        return self.القاعة

class مطلب_نشاط(models.Model):
    CHOICES = (
        ('طلبة من داخل المعهد','طلبة من داخل المعهد'),
        ('طلبة من داخل و خارج المعهد','طلبة من داخل و خارج المعهد'),
        ('كل الفئات','كل الفئات')
    )
    TYPE = (
        ('يوم مفتوح','يوم مفتوح'),('طلب دعم','طلب دعم'),('رحلة دراسية','رحلة دراسية'),('نشاط ثقافي','نشاط ثقافي')
        ,('نشاط رياضي','نشاط رياضي'),('نشاط علمي','نشاط علمي'),('رحلة ترفيهية','رحلة ترفيهية')

    )
    نشاط_عدد = models.CharField(max_length=255)
    تاريخ_بداية_النشاط =  models.DateField()
    تاريخ_نهاية_النشاط =  models.DateField()
    الزمان = models.TimeField()
    المكان = models.CharField(max_length=1000)
    الموضوع = models.CharField(max_length=1000)
    رئيس_النادي= models.CharField(max_length=255)     
    الفئة_المستهدفة = models.CharField(max_length=255, choices=CHOICES,default='طلبة من داخل المعهد')        
    نبذة_عن_النشاط = models.CharField(max_length=2000)   
    النادي=models.ForeignKey(بيانات_النادي, on_delete=models.CASCADE,null=True)
    نوع_النشاط= models.CharField(max_length=255,choices=TYPE,default='نشاط ثقافي')
    def __str__(self):
        return self.نشاط_عدد 

 




