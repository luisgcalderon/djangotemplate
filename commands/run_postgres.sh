podman run --name django_fs \
    -p 5432:5432 \
    -e POSTGRES_USER=django \
    -e POSTGRES_PASSWORD=django \
    -e POSTGRES_DB=django \
    -d postgres:13