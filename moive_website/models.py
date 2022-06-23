# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    name = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Collect(models.Model):
    user_id = models.PositiveIntegerField()
    type = models.IntegerField()
    song_id = models.PositiveIntegerField(blank=True, null=True)
    song_list_id = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'collect'


class Comment(models.Model):
    user_id = models.PositiveIntegerField()
    song_id = models.PositiveIntegerField(blank=True, null=True)
    song_list_id = models.PositiveIntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    up = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class Consumer(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=100)
    sex = models.IntegerField(blank=True, null=True)
    phone_num = models.CharField(unique=True, max_length=15, blank=True, null=True)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    introduction = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    avator = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'consumer'


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


class ListSong(models.Model):
    song_id = models.PositiveIntegerField()
    song_list_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'list_song'


class MovieMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    play_num = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    movie_file = models.CharField(max_length=255, blank=True, null=True)
    download_url = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    star = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_message'


class RankList(models.Model):
    id = models.BigAutoField(primary_key=True)
    songlistid = models.BigIntegerField(db_column='songListId')  # Field name made lowercase.
    consumerid = models.BigIntegerField(db_column='consumerId')  # Field name made lowercase.
    score = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'rank_list'
        unique_together = (('consumerid', 'songlistid'),)


class Singer(models.Model):
    name = models.CharField(max_length=45)
    sex = models.IntegerField(blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    introduction = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'singer'


class Song(models.Model):
    singer_id = models.PositiveIntegerField()
    name = models.CharField(max_length=45)
    introduction = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    pic = models.CharField(max_length=255, blank=True, null=True)
    lyric = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'song'


class SongList(models.Model):
    title = models.CharField(max_length=255)
    pic = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    style = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_list'
