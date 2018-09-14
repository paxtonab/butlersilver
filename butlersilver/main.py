import datetime
import insta
import models

from flask import Flask, flash, g, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, TextField, IntegerField, DateField, SelectMultipleField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, Length, EqualTo)

app = Flask(__name__)

today = datetime.datetime.today()
year = today.year
home = 'http://www.butlersilver.com'


@app.route('/')
def index():
    return render_template('index.html', gallery=models.Silver.get_featured_silver(), title="Butler Silver Gallery", year=year)

@app.route('/gallery')
def gallery_all():
    return render_template('gallery.html', gallery=models.Silver.get_silver(), title="Butler Silver Gallery", activeP=True, year=year)


@app.route('/about')
def about():
    return render_template('about.html', activeA=True, title="About Butler Silver", year=year)


@app.route('/contact')
def contact():
    return render_template('contact.html', activeC=True, title="Contact Butler Silver", year=year, instagram=insta.get_latest_insta())


@app.route('/repairs')
def repairs():
    return render_template('repairs.html', activeR=True, title="Silver Repairs & Appraisals", year=year)


@app.route('/gallery/<silver_permalink>-<silver_id>')
def gallery(silver_permalink, silver_id):
    return render_template('silver.html',
							gallery=silver[int(silver_id)],
							title="Butler Silver Gallery",
							activeP=True,
							year=year)



#@app.errorhandler(404)
#def page_not_found(e):
#    """Return a custom 404 error."""
#    return render_template('404.html', title='404: Page Not Found', year=year)
    #'Sorry, Nothing at this URL.', 404


#@app.errorhandler(500)
#def application_error(e):
#    """Return a custom 500 error."""
#    return 'Sorry, unexpected error: {}'.format(e), 500


@app.route('/workshop.html')
def workshop_redirect():
	return redirect(app.about(), code=301)

@app.route('/wine_coasters.html')
def wine_coasters_redirect():
	return redirect(app.index(), code=301)

@app.route('/animals.html')
def animals_redirect():
	return redirect(app.index(), code=301)

@app.route('/contact.html')
def contact_redirect():
	return redirect(app.contact(), code=301)

if __name__ == '__main__':
	models.initialize()
	models.Silver.initialize_silver()
	app.run()
