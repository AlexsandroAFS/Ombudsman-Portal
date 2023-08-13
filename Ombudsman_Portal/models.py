from django.db import models
from django.http import request
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class OmbudsmanTypeComplaint(models.Model):
    otc_title = models.CharField(max_length=100, verbose_name='Titulo')
    otc_description = models.CharField(max_length=250, verbose_name='Descrição')
    otc_create_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return str(self.otc_title)

    class Meta:
        verbose_name_plural = 'Tabela de Registro de Tipo de Denuncia'
        ordering = ['otc_title']


class OmbudsmanStatus(models.Model):
    user = get_user_model()
    ost_title = models.CharField(max_length=100, verbose_name='Título')
    ost_description = models.CharField(max_length=100, verbose_name='Descrição')
    ost_create_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return str(self.ost_title)

    class Meta:
        verbose_name_plural = 'Tabela de Registro de Status'
        ordering = ['ost_title']


class OmbudsmanPortalForm(models.Model):
    fm_name = models.CharField(max_length=999, blank=True, verbose_name='Nome')
    fm_email = models.CharField(max_length=999, blank=True, verbose_name='E-mail')
    fm_phone = models.CharField(max_length=999, blank=True, verbose_name='Telefone')
    fm_type_complaint = models.TextField(max_length=99999, blank=True, verbose_name='Tipo de Ocorrencia')
    fm_complaint_description = models.CharField(max_length=99999, verbose_name='Descrição da Ocorrencia')
    fm_complaint_datetime = models.DateTimeField(blank=False, verbose_name='Data da Ocorrencia')
    fm_status_complaint = models.ForeignKey(OmbudsmanStatus, blank=True, on_delete=models.DO_NOTHING)
    fm_date_create = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return str(self.fm_date_create) + ' ' + str(self.fm_status_complaint)

    class Meta:
        verbose_name_plural = 'Tabela para Registro de Ocorrencias'
        ordering = ['fm_date_create']
