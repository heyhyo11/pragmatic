# Generated by Django 4.2.11 on 2024-04-12 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0003_article_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_record', to='articleapp.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_record', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'article')},
            },
        ),
    ]
