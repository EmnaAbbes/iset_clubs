# Generated by Django 4.2.5 on 2023-10-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0006_remove_مطلب_نشاط_اسم_النادي_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='مطلب_نشاط',
            name='الفئة_المستهدفة',
            field=models.CharField(choices=[('طلبة من داخل المعهد', 'طلبة من داخل المعهد'), ('طلبة من داخل و خارج المعهد', 'طلبة من داخل و خارج المعهد'), ('كل الفئات', 'كل الفئات')], default='طلبة من داخل المعهد', max_length=255),
        ),
    ]
