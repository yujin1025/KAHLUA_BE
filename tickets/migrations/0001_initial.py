# Generated by Django 4.0 on 2023-07-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ticketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('member', models.PositiveIntegerField(default=0)),
                ('available_ticket', models.BooleanField(default=True)),
                ('meeting', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
