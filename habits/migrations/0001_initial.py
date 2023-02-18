# Generated by Django 4.1.6 on 2023-02-12 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('time', models.TimeField()),
                ('frequency', models.CharField(choices=[('daily', 'Everyday'), ('six times a week', 'Six times a week'), ('five times a week', 'Five times a week'), ('four times a week', 'Four times a week'), ('three times a week', 'Three times a week'), ('two times a week', 'Two times a week'), ('ones a week', 'Ones a week')], max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('category', models.CharField(choices=[('other', 'Other'), ('study', 'Study'), ('finance', 'Finance'), ('work', 'Work'), ('sport', 'Sport'), ('social', 'Social'), ('home', 'Home')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time', 'priority'],
            },
        ),
    ]