# Generated by Django 4.0.6 on 2023-02-01 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagerapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='displayusernames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
