Proof of concept running django and Recurly for payment.

Start running:
* Install pip
* Install virtualenv: pip install virtualenv
* Create virtualenv: virtualenv --no-site-packages venv
* Activate venv: source venv/bin/activate
* Install requirements: pip install -r requirements.txt
* Export environment variables:
  * RECURLY_PUBLIC # The recurly js api key
  * RECURLY_API # The main recurly api key
  * SUBDOMAIN # Recurly subdomain
* Create database: ./manage.py syncdb
* Start running: ./manage.py runserver 8000