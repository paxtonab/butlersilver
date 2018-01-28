import datetime
import insta
import urllib
from flask import Flask, flash, g, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, TextAreaField, TextField, IntegerField, DateField, SelectMultipleField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError,
								Email, Length, EqualTo)

app = Flask(__name__)

today = datetime.datetime.today()
year = today.year


home = 'http://www.butlersilver.com'

encoded_home = urllib.quote_plus(home)


silver1 = {'url':'img/butler-silver-sea-vase.jpg',
			'url_small':'img/butler-silver-sea-vase-small.jpg',
			'description':'Sea shell and coral vase.',
			'name':'Sterling Silver Sea Shell and Coral Vase',
			'permalink':'silver-sea-vase',
			'encoded_url': urllib.quote_plus(home+'/img/butler-silver-sea-vase.jpg'),
			'encoded_description': urllib.quote_plus('Sea shell and coral vase.'),
			'orginal_index':3}

silver2 = {'url':'img/butler-hair-comb.jpg',
			'url_small':'img/butler-hair-comb-small.jpg',
			'description':'Art-nouveau style hair comb. Private collection.',
			'name':'Sterling Silver Octopus Hair Comb',
			'permalink':'silver-hair-comb',
			'encoded_url': urllib.quote_plus(home+'/img/butler-hair-comb.jpg'),
			'encoded_description': urllib.quote_plus('Art-nouveau style hair comb. Private collection.')}

silver3 = {'url':'img/butler-penguin-bowl.jpg',
			'url_small':'img/butler-penguin-bowl-small.jpg',
			'description':'Penguin bowl. Private collection.',
			'name':'Sterling Silver Emperor Penguin Ice Bucket',
			'permalink':'silver-penguin-bowl',
			'encoded_url': urllib.quote_plus(home+'/img/butler-penguin-bowl.jpg'),
			'encoded_description': urllib.quote_plus('Penguin bowl. Private collection.'),
			'orginal_index':5}

silver4 = {'url':'img/butler-fish-slice.jpg',
			'url_small':'img/butler-fish-slice-small.jpg',
			'description':'Fish slice. Victoria and Albert Museum, London.',
			'name':'Sterling Silver Fish Slice',
			'permalink':'silver-fish-slice',
			'encoded_url': urllib.quote_plus(home+'/img/butler-fish-slice.jpg'),
			'encoded_description': urllib.quote_plus('Fish slice. Victoria and Albert Museum, London.')}

silver5 = {'url':'img/butler-silver-frog.jpg',
			'url_small':'img/butler-silver-frog-small.jpg',
			'description':'Sterling silver green frog.',
			'name':'Sterling Silver Green Frog',
			'permalink':'silver-frog',
			'encoded_url': urllib.quote_plus(home+'/img/butler-silver-frog.jpg'),
			'encoded_description': urllib.quote_plus('Silver green frog.')}

silver6 = {'url':'img/butler-acorn-oak-leaves-wine-coaster.jpg',
			'url_small':'img/butler-acorn-oak-leaves-wine-coaster-small.jpg',
			'description':'Acorn and oak leaf wine bottle coaster.',
			'name':'Sterling Silver Acorn and Oak Leaf Wine Bottle Coaster',
			'permalink':'silver-acorn-oak-leaves-wine-coaster',
			'encoded_url': urllib.quote_plus(home+'/img/butler-acorn-oak-leaves-wine-coaster.jpg'),
			'encoded_description': urllib.quote_plus('Acorn and oak leaf wine bottle coaster.')}

silver7 = {'url':'img/butler-mushroom-wine-coaster.jpg',
			'url_small':'img/butler-mushroom-wine-coaster-small.jpg',
			'description':'Mushroom wine bottle coaster.',
			'name':'Sterling Silver Mushroom Wine Bottle Coaster',
			'permalink':'silver-mushroom-wine-coaster',
			'encoded_url': urllib.quote_plus(home+'/img/butler-mushroom-wine-coaster.jpg'),
			'encoded_description': urllib.quote_plus('Mushroom wine bottle coaster.')}

silver8 = {'url':'img/butler-animal-bowl.jpg',
			'url_small':'img/butler-animal-bowl-small.jpg',
			'description':'Animal bowl. Museum of Fine Arts, Boston.',
			'name':'Sterling Silver African Plains Animal Punch Bowl',
			'permalink':'silver-animal-bowl',
			'encoded_url': urllib.quote_plus(home+'img/butler-animal-bowl.jpg'),
			'encoded_description': urllib.quote_plus('Animal bowl. Museum of Fine Arts, Boston.'),
			'orginal_index':4}

silver9 = {'url':'img/butler-silver-baby-cup.jpg',
			'url_small':'img/butler-silver-baby-cup-small.jpg',
			'description':'Baby cup with swan handle.',
			'name':'Sterling Silver Baby Cup with Swan Handle',
			'permalink':'silver-baby-cup',
			'encoded_url': urllib.quote_plus(home+'img/butler-silver-baby-cup.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Baby Cup with Swan Handle.')}

silver10 = {'url':'img/mice-and-cheese-silver-knife.jpg',
			'url_small':'img/mice-and-cheese-silver-knife-small.jpg',
			'description':'Sterling Silver Mouse & Cheese Knife.',
			'name':'Sterling Silver Mouse & Cheese, Cheese Knife',
			'permalink':'silver-cheese-knife',
			'encoded_url': urllib.quote_plus(home+'img/mice-and-cheese-silver-knife.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Mouse and Cheese Knife.')}

silver11 = {'url':'img/sterling-silver-elephant-baby-cup.jpg',
			'url_small':'img/sterling-silver-elephant-baby-cup-small.jpg',
			'description':'Sterling Silver Baby Cup with Elephant Handle.',
			'name':'Sterling Silver Baby Cup with Elephant Handle',
			'permalink':'silver-baby-cup-elephant-handle',
			'encoded_url': urllib.quote_plus(home+'img/sterling-silver-elephant-baby.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Baby Cup with Elephant Handle.')}

silver12 = {'url':'img/butler-sterling-silver-chased-pitcher.jpg',
			'url_small':'img/butler-sterling-silver-chased-pitcher-small.jpg',
			'description':'Sterling Silver Chased Pitcher. Private collection.',
			'name':'Sterling Silver Chased Pitcher',
			'permalink':'sterling-silver-chased-pitcher',
			'encoded_url': urllib.quote_plus(home+'img/butler-sterling-silver-chased-pitcher.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Chased Pitcher.')}

silver13 = {'url':'img/sterling-silver-animal-baby-cup.jpg',
			'url_small':'img/sterling-silver-animal-baby-cup-small.jpg',
			'description':'Sterling Silver Baby Cup.',
			'name':'Sterling Silver Baby Cup',
			'permalink':'sterling-silver-chased-pitcher',
			'encoded_url': urllib.quote_plus(home+'img/sterling-silver-animal-baby-cup-small.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Baby Cup.')}

silver14 = {'url':'img/mice-and-cheese-sterling-silver-box.jpg',
			'url_small':'img/mice-and-cheese-sterling-silver-box-small.jpg',
			'description':'Three Blind Mice & Cheese Box.',
			'name':'Three Blind Mice & Cheese Box',
			'permalink':'sterling-silver-three-blind-mice-cheese-box',
			'encoded_url': urllib.quote_plus(home+'img/mice-and-cheese-sterling-silver-box.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Baby Cup.')}

silver15 = {'url':'img/sterling-silver-flower-vase.jpg',
			'url_small':'img/sterling-silver-flower-vase-small.jpg',
			'description':'Sterling Silver Flower Vase.',
			'name':'Sterling Silver Flower Vase',
			'permalink':'flowers-sterling-silver-box',
			'encoded_url': urllib.quote_plus(home+'img/sterling-silver-flower-vase.jpg'),
			'encoded_description': urllib.quote_plus('Sterling Silver Flower Vase.')}


silver = [silver15,
			silver14,
			silver13,
			silver12,
			silver10,
			silver11,
			silver1,
			silver8,
			silver3,
			silver4,
			silver6,
			silver7,
			silver5,
			silver2,
			silver9]

silver_home = [silver1, #id = 3
				silver8, #id = 4
				silver3,] #id = 5


@app.route('/')
def index():
    return render_template('index.html', gallery=silver_home, title="Butler Silver Gallery", year=year)

@app.route('/gallery')
def gallery_all():
    return render_template('gallery.html', gallery=silver, title="Butler Silver Gallery", activeP=True, year=year)


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
    app.run()
