from google.appengine.ext import db
from string import letters
import datetime
import hashlib
import hmac
import jinja2
import random
import re
import os
import urllib
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
autoescape = True)

today = datetime.datetime.today()
year = today.year

home = 'http://valid-alpha-860.appspot.com'

encoded_home = urllib.quote_plus(home)


silver1 = {'url':'img/butler-silver-sea-vase.jpg',
			'description':'Sea shell and coral vase. Available.',
			'name':'Sterling Silver Sea Shell and Coral Vase',
			'permalink':'silver-sea-vase',
			'encoded_url': urllib.quote_plus(home+'/img/butler-silver-sea-vase.jpg'),
			'encoded_description': urllib.quote_plus('Sea shell and coral vase. Available.')}

silver2 = {'url':'img/butler-hair-comb.jpg',
			'description':'Art-nouveau style hair comb. Private Collection.',
			'name':'Sterling Silver Octopus Hair Comb',
			'permalink':'silver-hair-comb',
			'encoded_url': urllib.quote_plus(home+'/img/butler-hair-comb.jpg'),
			'encoded_description': urllib.quote_plus('Art-nouveau style hair comb. Private Collection.')}

silver3 = {'url':'img/butler-penguin-bowl.jpg',
			'description':'Penguin bowl. Private collection.',
			'name':'Sterling Silver Emperor Penguin Ice Bucket',
			'permalink':'silver-penguin-bowl',
			'encoded_url': urllib.quote_plus(home+'/img/butler-penguin-bowl.jpg'),
			'encoded_description': urllib.quote_plus('Penguin bowl. Private collection.')}

silver4 = {'url':'img/butler-fish-slice.jpg',
			'description':'Fish slice. Victoria and Albert Museum, London.',
			'name':'Sterling Silver Fish Slice',
			'permalink':'',
			'encoded_url': urllib.quote_plus(home+'/img/butler-fish-slice.jpg'),
			'encoded_description': urllib.quote_plus('Fish slice. Victoria and Albert Museum, London.')}

silver5 = {'url':'img/butler-silver-frog.jpg',
			'description':'Silver bull frog. Available.',
			'name':'Sterling Silver Green Frog',
			'permalink':'silver-frog',
			'encoded_url': urllib.quote_plus(home+'/img/butler-silver-frog.jpg'),
			'encoded_description': urllib.quote_plus('Silver green frog. Available.')}

silver6 = {'url':'img/butler-acorn-oak-leaves-wine-coaster.jpg',
			'description':'Acorn and oak leaf wine bottle coaster. Available.',
			'name':'Sterling Silver Acorn and Oak Leaf Wine Bottle Coaster',
			'permalink':'silver-acorn-oak-leaves-wine-coaster',
			'encoded_url': urllib.quote_plus(home+'/img/butler-acorn-oak-leaves-wine-coaster.jpg'),
			'encoded_description': urllib.quote_plus('Acorn and oak leaf wine bottle coaster. Available.')}

silver7 = {'url':'img/butler-mushroom-wine-coaster.jpg',
			'description':'Mushroom wine bottle coaster. Available.',
			'name':'Sterling Silver Mushroom Wine Bottle Coaster',
			'permalink':'silver-mushroom-wine-coaster',
			'encoded_url': urllib.quote_plus(home+'/img/butler-mushroom-wine-coaster.jpg'),
			'encoded_description': urllib.quote_plus('Mushroom wine bottle coaster. Available.')}
			
silver8 = {'url':'img/butler-animal-bowl.jpg',
			'description':'Animal bowl. Museum of Fine Arts, Boston.',
			'name':'Sterling Silver African Plains Animal Punch Bowl',
			'permalink':'silver-animal-bowl',
			'encoded_url': urllib.quote_plus(home+'img/butler-animal-bowl.jpg'),
			'encoded_description': urllib.quote_plus('Animal bowl. Museum of Fine Arts, Boston.')}

silver = [silver1, 
			silver8,
			silver3,
			silver4,
			silver6,
			silver7,
			silver5,
			silver2]

#class Silver(db.Model):
#	title = db.StringProperty()
#	picture = db.BlobProperty(default=None)
#	description = db.TextProperty(required = True)
#	created = db.DateTimeProperty(auto_now_add = True)
#	description_encoded = db.TextProperty(required = True)
#	url_encoded = db.TextProperty(required = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
		
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		
	def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)

class MainHandler(Handler):
    def render_front(self):
        self.render("index.html", gallery=silver, title="Butler Silver Gallery", year=year, activeP=True)
    
    def get(self):
        self.render_front()
        
class AboutHandler(Handler):
    def render_front(self):
    	self.render("about.html", title="About Butler Silver", year=year, activeA=True)
    
    def get(self):
        self.render_front()
        
class ContactHandler(Handler):
    def render_front(self):
    	self.render("contact.html", title="Contact Butler Silver", year=year, activeC=True)
    
    def get(self):
        self.render_front()
        
class ResumeHandler(Handler):
    def render_front(self):
    	self.render("repairs.html", title="Silver Repairs & Appraisals", year=year, activeR=True)
    
    def get(self):
        self.render_front()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler),
	('/repairs', ResumeHandler),
	webapp2.Route('/workshop.html', webapp2.RedirectHandler, defaults={'_uri':'/about'}),
	webapp2.Route('/wine_coasters.html', webapp2.RedirectHandler, defaults={'_uri':'/'}),
	webapp2.Route('/animals.html', webapp2.RedirectHandler, defaults={'_uri':'/'}),
	webapp2.Route('/contact.html', webapp2.RedirectHandler, defaults={'_uri':'/contact'})
], debug=True)
