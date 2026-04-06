# Usa la imagen base de SQL Server
FROM mcr.microsoft.com/mssql/server:2019-latest

# Cambia a root para instalar paquetes (el usuario por defecto es mssql)
USER root

# Instala las herramientas de SQL Server (sqlcmd)
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends mssql-tools18 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Vuelve al usuario mssql para que el servicio corra con los permisos correctos
USER mssql
# El CMD original de la imagen base se mantiene (inicia SQL Server)
