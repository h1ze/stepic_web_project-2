sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo pip istall django-autofixture
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database qa"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'qa_user'@'localhost' IDENTIFIED BY '123';"

#gunicorn -b 0.0.0.0:8080 hello:app
#./script.sh
