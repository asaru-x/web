sudo cp etc/nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx reload
sudo /etc/init.d/mysql start

mysql -u root -e "CREATE DATABASE stepik_web;"
mysql -u root -e "GRANT ALL PRIVILEGES ON stepik_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

gunicorn -D --bind 0.0.0.0:8080 hello:application
django-admin startproject ask
cd ask
./manage.py startapp qa
cd ../etc
cp settings.py urls.py ../ask/ask/
cp models.py views.py ../ask/qa/
cp -r templates/ ask/qa/
cd ../ask
./manage.py makemigrations
./manage.py migrate
gunicorn -D --bind 0.0.0.0:8000 ask.wsgi:application
