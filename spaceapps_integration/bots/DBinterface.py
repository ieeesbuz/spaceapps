#!/usr/bin/python3
# -*- coding: utf-8 -*-

import utils as ut

class nasaDBinterface(object):
	def __init__ (self):

		self.param_dic = {
		    "host"      : "192.168.0.120",
		    "database"  : "mydb",
		    "user"      : "postgres",
		    "password"  : "WoodenRumba00"
			}



	def get_ranking(self, number_cities, top_button=True):
		comm = ut.conexion(self.param_dic)
		
		ranking = None
		if comm != None: ranking = ut.get_ranking_arr(comm,number_cities, top_button)
		
		comm.close()

		return ranking

	def get_consulta(self, city_name):
		comm = ut.conexion(self.param_dic)
		
		city_info = None
		if comm != None: city_info = ut.get_city_info(comm,city_name)
		
		comm.close()

		return city_info

	def get_image(self):
		comm = ut.conexion(self.param_dic)
		
		image_dir = None
		if comm != None: image_dir = ut.create_image(comm)
		
		comm.close()

		return image_dir

	def get_city_image(self, name):
		image_dir = ut.create_city_image(name)

		return image_dir

	def get_plot(self,n_cities):
		comm = ut.conexion(self.param_dic)
		
		plot_dir = None
		if comm != None: plot_dir = ut.create_ranking_plot(comm,n_cities, True)
		
		comm.close()

		return plot_dir