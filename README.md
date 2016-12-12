Flask WS Template
================

Simple flask ws template with admin, and db.

~Under Construction~

Installation Process
-------------------

* Virtualenv
  ```bash
  sudo python3 -m pip install virtualenv virtualenvwrapper
  echo 'export WORKON_HOME="~/.virtualenvs"' >> ~/.bashrc
  echo 'export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python3"' >> ~/.bashrc
  echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bashrc
  source ~/.bashrc
  mkvirtualenv -ppython3 app
  workon app
  ```
* Application
  ```bash
  pip install -r requirements.txt 
  python app/app.py
  ```
