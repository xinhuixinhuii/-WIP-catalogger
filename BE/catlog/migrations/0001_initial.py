# Generated by Django 4.2 on 2023-04-21 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatLog',
            fields=[
                ('catlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catlist.catlist')),
                ('location', models.JSONField(max_length=128)),
                ('dateTime', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('catlist.catlist',),
        ),
    ]