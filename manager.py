# -*- coding: utf-8 -*-

import template
import database
import tables
import windows

class Manager (database.Data):
	def __init__(self, table, windows_dict):
		super().__init__(table, windows_dict)

	def open_home(self):
		self.url = 'home'
		self.display_help(self.url)

	def home(self):
		if self.event == '1':
			self.url = 'all_categories'
			self.display_help(self.url)
			self.get_category()
		elif self.event == '2':
			self.url = 'all_favorites'
			self.display_help(self.url)
			self.get_favorite()

	def all_categories(self):
		if self.event == 'r':
			self.open_home()
		elif int(str(self.event)) > 0:
			self.url = 'all_products'
			self.category_id = self.event
			self.display_help(self.url)
			self.get_product(self.category_id)

	def check_substitute(self):

		if int(str(self.substitute_id)) == 0:
			self.display_help(self.url)
			self.get_feature(self.product_id)
			self.select_substitute_list(self.category_id, self.product_id)
		elif int(str(self.substitute_id)) > 0:

			self.display_help(self.url)
			self.get_feature(self.product_id)
			self.select_substitute(self.substitute_id)

	def all_products(self):
		if self.event == 'r':
			self.url = 'all_categories'
			self.display_help(self.url)
			self.get_category()
		elif int(str(self.event)) > 0:
			self.url = 'product'
			self.product_id = self.event
			self.substitute_id = 0
			self.check_substitute()


	def product(self):
		if self.event == 'r':
			self.url = 'all_products'
			self.display_help(self.url)
			self.get_product(self.category_id)
			self.event = 0
		elif int(str(self.event)) > 0:
			self.url = 'product_substitute'
			self.substitute_id = self.event
			self.check_substitute()

	def product_substitute(self):
		if  self.event == 'e':
			self.save_product(self.product_id, self.substitute_id)
		elif self.event == 'r':
			self.url = 'product'
			self.substitute_id = 0
			self.check_substitute()

	def all_favorites(self):
		if self.event == 'r':
			self.url = 'open_home'
			self.open_home()
		elif int(str(self.event)) > 0:
			self.favorite_id = self.event
			self.url = 'favorite'
			self.display_help(self.url)
			self.select_feature_favorite(self.favorite_id)


	def favorite(self):
		if self.event == 'r':
			self.url = 'all_favorites'
			self.display_help(self.url)
			self.get_favorite()
		elif self.event == 's':
			self.delete_favorite(self.favorite_id)
		

	def main(self):

		self.open_home()
		while True:

			self.event = input("choix : ")

			if self.event == 'q':
				quit()

			elif self.url == 'home':
				self.home()
				self.event = 0

			elif self.url == 'all_categories':
				self.all_categories()
				self.event = 0
			
			elif self.url == 'all_products':
				self.all_products()
				self.event = 0

			elif self.url == 'product':
				self.product()
				self.event = 0

			elif self.url == 'product_substitute':
				self.product_substitute()
				self.event = 0

			elif self.url == 'all_favorites':
				self.all_favorites()
				self.favorite_id = self.event
				self.event = 0

			elif self.url == 'favorite':
				self.favorite()
				self.event = 0











