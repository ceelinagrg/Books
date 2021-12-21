# Generated by Django 3.2.9 on 2021-12-01 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=50)),
                ('hgender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heroinfos', to='books.book')),
            ],
        ),
    ]
