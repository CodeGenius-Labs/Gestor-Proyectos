# Usa una imagen ligera de Python como base
FROM python:3.10-slim

# Instala las dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    libmariadb-dev-compat \
    && apt-get clean

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instálalos
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . /app

# Expone el puerto por defecto de Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
