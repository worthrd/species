FROM postgres:alpine
ENV POSTGRES_PASSWORD=342516
ENV POSTGRES_USER=recep
ENV POSTGRES_DB=species
RUN mkdir -p /var/lib/postgresql/tsvs
COPY pgdata/NameUsage.tsv /var/lib/postgresql/tsvs
COPY init.sql /docker-entrypoint-initdb.d/init.sql