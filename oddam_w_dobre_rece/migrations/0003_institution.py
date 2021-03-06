# Generated by Django 3.0.5 on 2020-04-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam_w_dobre_rece', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('type', models.CharField(choices=[('fundacja', 'fundacja'), ('organizacja pozarządowa', 'organizacja pozarządowa'), ('zbórka lokalna', 'zbórka lokalna')], default='fundacja', max_length=32)),
            ],
        ),
    ]
