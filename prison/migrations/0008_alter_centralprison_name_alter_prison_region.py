# Generated by Django 4.1 on 2022-10-10 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0007_alter_centralprison_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centralprison',
            name='Name',
            field=models.CharField(choices=[('Amhara Region Prison Police', 'Amhara Region Prison Police')], default='Amhara Region Prison Police', max_length=100),
        ),
        migrations.AlterField(
            model_name='prison',
            name='Region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prison.centralprison'),
        ),
    ]
