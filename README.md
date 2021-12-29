# Prueba técnica para Destacame.cl

Antes que nada, espero que les guste!

### Requerimiento

Una agencia de buses necesita una plataforma para gestionar sus viajes. El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen la misma capacidad de 10 pasajeros sentados. Los asientos son numerados y se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular, además de permitir la asignación de choferes a sus respectivos buses.

### Backend

Si usted estuviera resolviendo el problema de la agencia de buses implementando una aplicación web que incluya las siguientes funcionalidades:

- CRUD pasajeros, choferes, trayectos, buses.
- Listar los trayectos junto a su promedio de pasajeros.
- Filtrar a todos los buses de un trayecto con más del N % de su capacidad vendida.
- Para la implementación hay que utilizar el Django y su ORM.

## Instalacion dependencias del Backend

## Features

- [Python 3.10.1](https://www.python.org/downloads/)

## Como instalar

Desde el directorio principal del proyecto ejecutar el siguiente comando para crear un entorno virtual:

```bash
pip install virtualenv
python -m virtualenv backend/env
```

Luego ejecutar este comando para instalar las dependencias del backend:

```bash
pip install -r requirements.txt 
```

Antes de levantar el servidor hay que realizar una migracion para propagar los modelos en el esquema de la base de datos:

```bash
py manage.py makemigrations
py manage.py migrate
```

## Deployment

Poner en marcha servidor:

```bash
py manage.py runserver
```

## Instalacion dependencias del Frontend

## Features

- [Node js 16.13.1](https://nodejs.org/es/download/)

## Como instalar

Para instalar las dependencias de nuestra aplicacion, desde el directorio principal del proyecto ejecutar el siguiente comando:

```bash
cd frontend/
npm install
```

## Deployment

Para poner en marcha el servidor:

```bash
npm run dev
```