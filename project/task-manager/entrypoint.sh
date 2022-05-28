#!/bin/sh

python src/manage.py flush --no-input
python src/manage.py migrate

# python src/manage.py run_consumer
exec "$@"
