# Generated by Django 3.1 on 2020-08-26 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.language'),
        ),
    ]