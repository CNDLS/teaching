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

## Deployment
* To create the static build: `python freeze.py`. This will create a directory called `build` which can then be uploaded directly to the serveer.
* After running `python freeze.py`, copy the contents of the `/build/` directory of this repository to the server directory, using SFTP or SSH.
* All pages in the ./pages/ directory will be built when you run Frozen Flask.
* There is also a deploy script in /deploy-scripts/.
* For it to work correctly, you must have a config.sh file in /deploy-scripts/ with the correct config variables.
  * See Brian Blosser if you need a copy of config.sh.
* To run it:
```
# Commit your changes
git commit -am "My new change"

# Push the change to origin
git push origin master

cd deploy-scripts

# Execute the deploy script - it will ask for your server password twice
# (once for ssh and once for rsync using ssh)
./deploy.sh
```

## Editing Site Content
* The content for this site is stored in HTML files ("flatpages") in the ./pages/ directory.
* [Flask Flatpages Documenation](http://flask-flatpages.readthedocs.io/en/latest/)
* Highlights
  * Page url structure comes from the folder structure and file names relative to the ./pages/ directory. For example, ./pages/design/assesment.html results in the url http://hostname/design/assessment/.
  * Each file is made of a YAML mapping of metadata, a blank line, and the page body, for example:
    ```YAML
    title: Hello
    published: 2010-12-22

    Hello, *World*!

    Lorem ipsum dolor sit amet, …
    ```
  * The default format for the flatpage body is Markdown, however...
  * This site sets the configuation setting FLATPAGES_HTML_RENDERER to use the Jinja2 templating engine, so you can use HTML and [Jinja2 template tags](http://jinja.pocoo.org/docs/2.10/templates/) inside the flatpage body.
  * You can even mix Jinja 2 and Markdown, which is why many of the flatpages have some content in Markdown, and some in HTML.
  * As of 08/21/2018, Brian Blosser is moving to have all page bodies be in only HTML, for consistency.

## URL Routing
* [How to define routes in Flask](http://flask.pocoo.org/docs/1.0/quickstart/#routing)
* URL routing and assigning templates to pages occurs in the file teaching.py.
* In this app, flatpages use a default template unless the 'template' meta key is defined in the flatpage.
* As of this writing (07/25/2018), only two templates are being used: templates/index.html and templates/handbook/detail.html (which extends other parent templates)

## Code Style
* HTML: Use this style guide: https://github.com/CNDLS/code-standards/blob/master/html.html
