# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AccountEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser')
    email = models.CharField(max_length=75)
    verified = models.BooleanField()
    primary = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'account_emailaddress'

class AccountEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)
    email_address = models.ForeignKey(AccountEmailaddress)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class Ingrediente(models.Model):
    idingrediente = models.IntegerField(unique=True)
    articulo = models.CharField(max_length=1024, blank=True)
    marca = models.CharField(max_length=1024, blank=True)
    tipo = models.CharField(max_length=1024, blank=True)
    codigobarras = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    establecimiento = models.CharField(max_length=1024, blank=True)
    precio = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ingrediente'

class IngredienteXReceta(models.Model):
    idingrediente = models.ForeignKey(Ingrediente, db_column='idingrediente')
    idreceta = models.ForeignKey('Receta', db_column='idreceta')
    class Meta:
        managed = False
        db_table = 'ingrediente_x_receta'

class Pasos(models.Model):
    idpaso = models.IntegerField(unique=True)
    idreceta = models.ForeignKey('Receta', db_column='idreceta', blank=True, null=True)
    pasonumero = models.IntegerField(blank=True, null=True)
    contenido = models.CharField(max_length=1024, blank=True)
    class Meta:
        managed = False
        db_table = 'pasos'

class Receta(models.Model):
    idreceta = models.IntegerField(unique=True)
    idrecetario = models.ForeignKey('Recetario', db_column='idrecetario', blank=True, null=True)
    nombre = models.CharField(max_length=1024, blank=True)
    tiempo = models.CharField(max_length=1, blank=True)
    descripcion = models.CharField(max_length=1024, blank=True)
    class Meta:
        managed = False
        db_table = 'receta'

class Recetario(models.Model):
    idrecetario = models.IntegerField(unique=True)
    idusuario = models.ForeignKey(AuthUser, db_column='idusuario', blank=True, null=True)
    nombrer = models.CharField(max_length=1024, blank=True)
    descripcionr = models.CharField(max_length=1024, blank=True)
    class Meta:
        managed = False
        db_table = 'recetario'

class SocialaccountSocialaccount(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=255)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'

class SocialaccountSocialapp(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'

class SocialaccountSocialappSites(models.Model):
    id = models.IntegerField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp)
    site = models.ForeignKey(DjangoSite)
    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'

class SocialaccountSocialtoken(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.ForeignKey(SocialaccountSocialapp)
    account = models.ForeignKey(SocialaccountSocialaccount)
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'

