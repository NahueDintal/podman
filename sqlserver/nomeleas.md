Para correr el contenedor con las variables de entorno.

podman run -d --name sqlserver --env-file .env -p 1433:1433 mcr.microsoft.com/mssql/server:2019-latest

para poder ejercutar el cmd de sql

/opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -P "Passw0rd" -C


