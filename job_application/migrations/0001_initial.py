# Generated by Django 4.2.1 on 2023-06-07 06:04

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
            name='job_applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_url', models.TextField(max_length=100)),
                ('next_event_date', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Under Consideration', 'Under Consideration'), ('Interview', 'Interview'), ('Declined', 'Declined'), ('Accepted', 'Accepted')], default='Applied', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]