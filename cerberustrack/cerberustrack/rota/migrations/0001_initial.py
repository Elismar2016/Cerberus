# Generated by Django 5.1.2 on 2025-01-20 15:41

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('odometro', models.IntegerField()),
                ('status', models.CharField(choices=[('em manutenção', 'Em manutenção'), ('em revisão', 'Em revisão'), ('disponível', 'Disponível')], default='disponível', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('supervisor', 'Supervisor'), ('motorista', 'Motorista')], default='motorista', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='Os grupos aos quais o usuário pertence.', related_name='customuser_groups', to='auth.group', verbose_name='grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permissões específicas para o usuário.', related_name='customuser_permissions', to='auth.permission', verbose_name='permissões de usuário')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('cnh', models.CharField(max_length=12, unique=True)),
                ('categoria', models.CharField(max_length=2)),
                ('validade_cnh', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
                ('user', models.OneToOneField(limit_choices_to={'user_type': 'motorista'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=12, unique=True)),
                ('user', models.OneToOneField(limit_choices_to={'user_type': 'supervisor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=255)),
                ('odometro_inicial', models.IntegerField(editable=False)),
                ('data_partida', models.DateTimeField()),
                ('odometro_final', models.IntegerField(blank=True, null=True)),
                ('data_chegada', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('em andamento', 'Em andamento'), ('finalizada', 'Finalizada'), ('agendada', 'Agendada'), ('cancelada', 'Cancelada')], default='agendada', max_length=20)),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rota.motorista')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rota.veiculo')),
            ],
            options={
                'verbose_name': 'Viagem',
                'verbose_name_plural': 'Viagens',
            },
        ),
    ]
