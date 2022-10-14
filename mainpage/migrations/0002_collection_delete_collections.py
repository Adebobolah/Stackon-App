# Generated by Django 4.1.2 on 2022-10-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('open_price', models.IntegerField()),
                ('tweets', models.IntegerField()),
                ('sentiment', models.CharField(max_length=200)),
                ('nft_index', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Collections',
        ),
    ]
