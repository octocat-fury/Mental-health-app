# Generated by Django 5.1.3 on 2025-01-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harmonix', '0005_anxietytestresponse_delete_mentalhealthresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='sentiment_score',
            field=models.FloatField(default=0.0),
        ),
    ]
