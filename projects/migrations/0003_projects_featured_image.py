# Generated by Django 5.0.6 on 2024-06-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_projects_vote_ratio_projects_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
