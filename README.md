# RandomNumbersApiDjango
-----------------------

### Setup Guide

#### 1. Windows
- Make sure you have python installed
- Double click the `server.bat` and wait for it to start the server.
- Double click on `client.bat` to start Microsoft Edge on http://127.0.0.1:8000/

#### 2. Linux
- Ubuntu
  - Run commands
     ```bash
        $ sudo apt install python3-virtualenv
        $ python3 -m virtualenv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
        $ python manage.py runserver
      ``` 
  - Start your browser on http://127.0.0.1:8000/
  

- Fedora / openSUSE / Redhat / CentOS
  - Run commands
    ```bash 
    $ pip install virtualenv
    $ python -m virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver
    ```
  - Start your browser on http://127.0.0.1:8000/
