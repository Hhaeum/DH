# Generated by Django 2.2.3 on 2019-08-06 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dongne1', '0002_auto_20190806_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dongne1',
            new_name='Dongne1',
        ),
        migrations.AlterField(
            model_name='comment',
            name='Dongne1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongne1.Dongne1'),
        ),
    ]
