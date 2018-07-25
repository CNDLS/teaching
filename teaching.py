import os
from flask import Flask, render_template, Markup, render_template_string, url_for
from flask.views import MethodView
from flask_flatpages import FlatPages, pygmented_markdown
from flaskext.mysql import MySQL

# create the application
app = Flask(__name__)
pages = FlatPages(app)

# define a custom renderer to enable url_for in flatpages
def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

APP_PREFIX='/teaching/'
app.config.update(dict(
    # MYSQL_DATABASE_USER = 'root',
    # MYSQL_DATABASE_DB = 'teaching',
    FREEZER_DESTINATION = 'build',
    FREEZER_DESTINATION_IGNORE = ['.GIT*', 'CNAME', '.gitignore', 'readme.md'],
    FREEZER_BASE_URL = 'http://localhost' + APP_PREFIX,
    FREEZER_RELATIVE_URLS = False,
    FLATPAGES_HTML_RENDERER = prerender_jinja,
))
app.config.from_envvar('TC_SETTINGS', silent=True)

# initialize the MySQL extension
from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)

def query_db(query, args=(), one=False):
    cur = mysql.get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    design_pages = (p for p in pages if 'design' in p.path[:6])
    design_page_list = sorted(design_pages, key=lambda p: p.meta['order'])
    teach_pages = (p for p in pages if 'teach' in p.path[:5])
    teach_page_list = sorted(teach_pages, key=lambda p: p.meta['order'])
    template = page.meta.get('template', 'handbook/detail.html')
    return render_template(template, page=page, design_page_list=design_page_list, teach_page_list=teach_page_list)

if __name__ == '__main__':
    app.run(debug=False)