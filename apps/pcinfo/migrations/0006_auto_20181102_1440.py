# Generated by Django 2.0 on 2018-11-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcinfo', '0005_auto_20181028_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcinfo',
            name='server_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.Servefactoryrinfo', verbose_name='制造商'),
        ),
    ]
