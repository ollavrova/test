This project implementing a URL shortening system with pyshorteners package.

Before start should to create users with commands - "manage.py create_fake_users -n 50", where n=50 is number of users. Number must be less than 10000.

###Urls:

* / - main page with submit form
* /!link - link info


###Requirements:

* Django 1.8+
* requests
* pyshorteners
* sqlite db
* Python 2.7