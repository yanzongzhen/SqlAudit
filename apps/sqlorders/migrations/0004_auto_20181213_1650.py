# Generated by Django 2.1.2 on 2018-12-13 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0003_auto_20181213_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysqlconfig',
            name='envi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sqlorders.SqlOrdersEnvironment', verbose_name='环境'),
        ),
    ]
