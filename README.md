Created by following the Django MongoDB Backend quickstart on dev.to. 

To start:
=========
```shell
pip install -r requirements.txt
```
Edit the DATABASES setting in `quickstart/settings.py`. Don't forget to edit the connection string to contain `sample_mflix`. 

```shell
python manage.py runserver
```

Quick Links
===========

- [Recent Movies](http://127.0.0.1:8000/recent_movies/)
- [Viewers](http://127.0.0.1:8000/viewers_list/)
- [Admin Page](http://127.0.0.1:8000/admin/)

To add more data:
=================

Edit `write_data.py` as needed.

```shell
python manage.py shell < write_data.py
```