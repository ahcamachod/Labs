from pandas import DataFrame
from datetime import datetime
import os

class Params:
	"""
	Parameters class.

	This file centralizes anything that can be 
	parametrized in the code.
	"""

	raw_data = f'../data/raw/raw_data{datetime.now().strftime("%Y-%m-%d")}.csv'
	external_data = '../data/external/'
	processed_data = '../data/processed/'
	intermediate_data = f'../data/raw/raw_data{datetime.now().strftime("%Y-%m-%d")}.csv'

	log_name = '../log/dump.log'

	# if this is set to True, then all the nodes will be automatically 
	# considered not up-to-date and will be rerun.
	rerun = True 

	## Database connection params
	
	user = 'postgres'
	password = '6324acsh'
	host = 'localhost'
	database = 'cinemark1'
	url = f'https://www.cinemark.com.br/sao-paulo/filmes/em-cartaz'