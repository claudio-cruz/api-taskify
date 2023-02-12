# Generated by Django 4.1.6 on 2023-02-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('other', 'Other'), ('study', 'Study'), ('finance', 'Finance'), ('work', 'Work'), ('sport', 'Sport'), ('social', 'Social'), ('home', 'Home')], max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10),
        ),
    ]
