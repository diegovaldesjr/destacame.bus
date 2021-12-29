from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.timezone import localtime

# Create your models here.
class Terminal(models.Model):
    alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')

    id = models.AutoField(primary_key = True)
    pais = models.CharField(max_length = 100, validators=[alphaSpaces])
    ciudad = models.CharField(max_length = 100, validators=[alphaSpaces])
    class Meta:
        unique_together = ["pais", "ciudad"]

class Chofer(models.Model):
    alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')

    rut = models.CharField(primary_key = True, max_length = 15)
    nombre = models.CharField(max_length = 100, validators=[alphaSpaces])
    apellido = models.CharField(max_length = 100, validators=[alphaSpaces])

class Bus(models.Model):
    placa = models.CharField(primary_key=True, max_length=15)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE, null=True)

class Asiento(models.Model):
    id = models.AutoField(primary_key = True)
    n_asiento = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    class Meta:
        unique_together = ["n_asiento", "bus"]

class Trayecto(models.Model):
    id = models.AutoField(primary_key = True)
    origen = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='origen')
    destino = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name='destino')
    class Meta:
        unique_together = ["origen", "destino"]

class Horario(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateTimeField()
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    class Meta:
        unique_together = ["fecha", "trayecto", "bus"]

class UserProfileManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            return ValueError('Usuario debe tener un email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nombre, password):
        user = self.create_user(email, nombre, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')

    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=50, validators=[alphaSpaces])
    # apellido = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def get_full_name(self):
        return self.nombre
    
    def __str__(self):
        return self.email

class Pasajero(models.Model):
    alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')

    id = models.AutoField(primary_key = True)
    email = email = models.EmailField(unique=True, max_length=255)
    nombre = models.CharField(max_length=50, validators=[alphaSpaces])
    apellido = models.CharField(max_length=50, validators=[alphaSpaces])

class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, null=True)
    class Meta:
        unique_together = ["horario", "trayecto", "asiento"]