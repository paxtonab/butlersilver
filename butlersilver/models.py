import datetime
import json
import urllib

from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

DATABASE = SqliteDatabase('debates.db')


class Silver(Model):
	permalink = CharField(unique=True)
	name = CharField(null=False)
	description = IntegerField(null=False)
	url = CharField(null=False)
	url_small= CharField(null=True)
	created = DateField(null=False)
	featured = BooleanField(null=False)

	class Meta:
		database = DATABASE
		order_by = ('featured','created',)


	@classmethod
	def initialize_silver(cls):
		with DATABASE.transaction():
			with open('silver.json') as f:
				silver_json = json.load(f)
			for silver in silver_json:
				try:
					if silver_json[silver]['featured'] is not None:
						featured_silver = True
					else:
						featured_silver = False
					cls.create(
								permalink = silver_json[silver]['permalink'],
								name = silver_json[silver]['name'],
								description = silver_json[silver]['description'],
								url = silver_json[silver]['url'],
								url_small= silver_json[silver]['url_small'],
								created = datetime.now(),
								featured = featured_silver
								)
				except IntegrityError:
					raise ValueError("Silver exists {}".format(silver['permalink']))


	@classmethod
	def get_silver(cls):
		"""
		:ret : file_list list of debate file names
		"""
		silver = cls.select()
		silver_list = []
		[silver_list.append(model_to_dict(s)) for s in silver]
		return silver_list

	@classmethod
	def get_featured_silver(cls):
		"""
		:ret : file_list list of debate file names
		"""
		silver = cls.select()
		silver_list = []
		[silver_list.append(model_to_dict(s)) for s in silver if s.featured == True]
		return silver_list

	@classmethod
	def encode_for_sharing(cls, string_for_encoding, url=False):
		"""
		Encode a string for sharing
		:ret encoded_string: encoded string
		"""
		encoded_string = urllib.quote_plus(string_for_encoding)
		return encoded_string


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Silver], safe=True)
	DATABASE.close()
