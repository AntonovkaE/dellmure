# Generated by Django 3.1.6 on 2021-03-10 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_shop', '0016_auto_20210306_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Товар с размером', 'verbose_name_plural': 'Товар с размером'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AddField(
            model_name='size',
            name='clothe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_shop.product'),
        ),
        migrations.AddField(
            model_name='size',
            name='index_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
