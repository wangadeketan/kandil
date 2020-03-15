# Generated by Django 2.2.6 on 2019-10-17 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=12000)),
                ('price', models.IntegerField(default=1)),
                ('photo', models.ImageField(upload_to='images/')),
                ('date', models.DateField(auto_now_add=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
    ]
