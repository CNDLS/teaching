# The Teaching Commons
## Site Info
* URL: https://commons.georgetown.edu/teaching/
* Server: CNDLS-LUX
* Server Location: `/var/www/docroot-ocw/teaching`

## Installation
* First, you'll need to set up a Python virtual environment. I usually do this in a directory called `.venv` in my home directory.
* Create the virtual environment: `cd teaching; virtualenv .venv;`
* Activate the virtual environment: `source .venv/bin/activate`
* Optional: Add an alias to your ``~/.bash_profile`` file that will let you just type `teaching` at the prompt to activate the virtual environment and run the Teaching Commons site: `alias teaching="cd /Users/yourusername/Sites/teaching/; source .venv//bin/activate; python teaching.py"` Then close and reopen your shell. Now you should have the `teaching` command available.
* Install Flask: `pip install flask`
* Install Flask-FlatPages: `pip install flask-flatpages`
* Install Frozen-Flask: `pip install frozen-flask`
* Install flask-mysql: `pip install flask-mysql`

## Running the development server
* In the project root: `python teaching.py`
* To create the static build: `python freeze.py`. This will create a directory called `build` which can then be uploaded directly to the serveer.

## Deployment
* After running `python freeze.py`, copy the contents of the `/build/` directory of this repository to the server directory, using SFTP or SSH.
