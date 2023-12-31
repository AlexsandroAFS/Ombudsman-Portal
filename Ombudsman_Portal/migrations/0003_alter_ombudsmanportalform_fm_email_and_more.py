# Generated by Django 4.2.3 on 2023-08-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ombudsman_Portal', '0002_alter_ombudsmanportalform_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ombudsmanportalform',
            name='fm_email',
            field=models.CharField(blank=True, max_length=999, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='ombudsmanportalform',
            name='fm_name',
            field=models.CharField(blank=True, max_length=999, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='ombudsmanportalform',
            name='fm_phone',
            field=models.CharField(blank=True, max_length=999, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='ombudsmanportalform',
            name='fm_status_complaint',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Ombudsman_Portal.ombudsmanstatus'),
        ),
        migrations.AlterField(
            model_name='ombudsmanportalform',
            name='fm_type_complaint',
            field=models.TextField(blank=True, max_length=99999, verbose_name='Tipo de Ocorrencia'),
        ),
    ]
