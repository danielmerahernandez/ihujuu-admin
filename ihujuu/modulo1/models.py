# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artistas(models.Model):
    idartistas = models.IntegerField(primary_key=True)
    nombre_artista = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    nacionalidad = models.CharField(max_length=45)
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    foto = models.CharField(max_length=45)
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')
    tipo_artista_idtipo_artista = models.ForeignKey('TipoArtista', models.DO_NOTHING, db_column='tipo_artista_idtipo_artista')

    class Meta:
        managed = False
        db_table = 'artistas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cronograma(models.Model):
    idcronograma = models.AutoField(primary_key=True)
    h_presentacion = models.CharField(max_length=45)
    eventos_ideventos = models.ForeignKey('Eventos', models.DO_NOTHING, db_column='eventos_ideventos')
    artistas_idartistas = models.ForeignKey(Artistas, models.DO_NOTHING, db_column='artistas_idartistas')

    class Meta:
        managed = False
        db_table = 'cronograma'


class Departamento(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_idmunicipio')

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    idempresa = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    eslogan = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    horario = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    logo = models.CharField(max_length=100)
    celular = models.IntegerField()
    telefono_fijo = models.IntegerField()
    eventos_ideventos = models.ForeignKey('Eventos', models.DO_NOTHING, db_column='eventos_ideventos')
    tipo_empresa_idtipo_empresa = models.ForeignKey('TipoEmpresa', models.DO_NOTHING, db_column='tipo_empresa_idtipo_empresa')
    pais_idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_idpais')

    class Meta:
        managed = False
        db_table = 'empresa'


class Eventos(models.Model):
    ideventos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.CharField(max_length=45)
    fecha_fin = models.CharField(max_length=45)
    imagen = models.CharField(max_length=45)
    hora_inicio = models.CharField(max_length=45)
    hora_fin = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'eventos'


class Municipio(models.Model):
    idmunicipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    barrio_idbarrio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipio'


class Pais(models.Model):
    idpais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_iddepartamento')

    class Meta:
        managed = False
        db_table = 'pais'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombre1 = models.CharField(max_length=45)
    nombre2 = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    ciudad = models.CharField(max_length=45)
    tipopersona_idtipopersona = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='tipopersona_idtipopersona')

    class Meta:
        managed = False
        db_table = 'persona'


class TipoArtista(models.Model):
    idtipo_artista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_artista'


class TipoEmpresa(models.Model):
    idtipo_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_empresa'


class TipoEvento(models.Model):
    id_tipo_evento = models.IntegerField(primary_key=True)
    descripcion_tipo_evento = models.CharField(max_length=45)
    categoria_tipo_evento = models.CharField(max_length=45)
    eventos_ideventos = models.ForeignKey(Eventos, models.DO_NOTHING, db_column='eventos_ideventos')

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class Tipopersona(models.Model):
    idtipopersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipopersona'
