web: gunicorn -w ${WORKERS:-1} -b "0.0.0.0:$PORT" main:app --timeout=1200  --log-level=${LOG_LEVEL:-debug}
