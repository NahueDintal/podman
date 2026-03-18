#!/bin/sh
# Reemplazar marcadores en index.html
sed -i "s/__HOSTNAME__/$(hostname)/g" /usr/share/nginx/html/index.html
sed -i "s/__MENSAJE__/${MENSAJE:-default}/g" /usr/share/nginx/html/index.html
# Ejecutar nginx
exec nginx -g 'daemon off;'
