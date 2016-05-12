Requirements
------------
* Flask
* Flask-FlatPages
* Frozen-Flask
* flask-mysql

Installation
------------
* First, you'll need to set up a Python virtual environment. I usually do this in a directory called ``.src`` in my home directory.
* Create the virtual environment: ``virtualenv flask``
* Activate the virtual environment: ``source flask/bin/activate``
* Optional: Add an alias to your ``~/.bash_profile`` file that will let you just type ``flask`` at the prompt to activate the virtual environment: ``alias flask="source /Users/yourusername/.src/flask/bin/activate"`` Then close and reopen your shell. Now you should have the ``flask`` command available.
* Install Flask: ``pip install flask``
* Install Flask-FlatPages: ``pip install flask-flatpages``
* Install Frozen-Flask: ``pip install frozen-flask``
* Install flask-mysql: ``pip install flask-mysql``

Running the development server
------------------------------
* In the project root: ``python teaching.py``
* To create the static build: ``python freeze.py``. This will create a directory called ``build`` which can then be uploaded directly to the spot on cndls-lux where the Teaching Commons site is deployed: ``/var/www/docroot-ocw/teaching``.