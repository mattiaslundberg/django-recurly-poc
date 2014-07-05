[![Build Status](https://api.travis-ci.org/mattiaslundberg/django-recurly-poc.png?branch=master)](https://travis-ci.org/mattiaslundberg/django-recurly-poc)

Proof of concept running django with [Recurly](http://recurly.com/) for payment.

Start running:
* Install pip for Python 2.7
* Install virtualenv: pip install virtualenv
* Create virtualenv: virtualenv --no-site-packages venv
* Activate virtualenv: source venv/bin/activate
* Install requirements: pip install -r requirements.txt
* Create a Recurly account with a plan called “haxxor”
* Export environment variables can be found when logged in to recurly:
  * RECURLY_PUBLIC # The recurly js api key (used for recurly.js)
  * RECURLY_API # The main recurly api key
  * SUBDOMAIN # Recurly subdomain
* Create database: ./manage.py syncdb
* Start running: ./manage.py runserver 8000
