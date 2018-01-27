FROM mysql

# Environment Variables
ENV MYSQL_ROOT_PASSWORD root

ADD ../../data/weather_data /
ADD init_scripts /docker-entrypoint-initdb.d
