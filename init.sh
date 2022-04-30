gunicorn -D --bind 0.0.0.0:8080 hello:application
cd ask
gunicorn -D --bind 0.0.0.0:8000 ask.wsgi:application
