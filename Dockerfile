FROM nginx:alpine 
COPY entrypoint.sh /entrypoint.sh
COPY website/index.html /usr/share/nginx/html/index.html
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
