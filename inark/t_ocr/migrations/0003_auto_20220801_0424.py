# Generated by Django 3.2.6 on 2022-08-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_ocr', '0002_auto_20220730_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrtext',
            name='biz_process',
            field=models.CharField(max_length=200, null=True, verbose_name='Business Process'),
        ),
        migrations.AddField(
            model_name='ocrtext',
            name='doc_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Document Name'),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Input Image'),
        ),
    ]
