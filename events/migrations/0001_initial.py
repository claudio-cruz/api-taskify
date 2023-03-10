# Generated by Django 4.1.6 on 2023-02-12 15:39

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('repeat', models.CharField(choices=[('none', 'No repeat'), ('daily', 'Everyday'), ('weekly', 'Once a Week'), ('monthly', 'Once a Month'), ('yearly', 'Once a Year')], default='none', max_length=10)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10)),
                ('category', models.CharField(choices=[('other', 'Other'), ('study', 'Study'), ('finance', 'Finance'), ('work', 'Work'), ('sport', 'Sport'), ('social', 'Social'), ('home', 'Home')], default='other', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start_time', 'priority'],
            },
        ),
    ]
