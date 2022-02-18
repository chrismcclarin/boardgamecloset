# Generated by Django 4.0.2 on 2022-02-18 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_salelocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salelocation',
            name='game',
        ),
        migrations.AddField(
            model_name='games',
            name='sale',
            field=models.ManyToManyField(to='main_app.SaleLocation'),
        ),
        migrations.CreateModel(
            name='GameTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('timeplayed', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.games')),
            ],
        ),
    ]