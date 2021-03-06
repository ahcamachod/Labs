import logging
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

logger = logging.getLogger('nodes.data_gathering')


def update(client, params):
	response = requests.get(params.url)
	soup = BeautifulSoup(response.content, 'lxml')
	movie_names = [movie.find('a')['title'].replace('Filme ','') for movie in soup.find_all('div', attrs={'class':'col-sm-6 col-md-3'})]
	movie_links = ['https://www.cinemark.com.br/' + movie.find('a')['href'] for movie in soup.find_all('div', attrs={'class':'col-sm-6 col-md-3'})]

	classificacao = []
	trailers = []
	duracao = []

	# run through the movies and get some info from it.
	df = pd.DataFrame()
	for link in movie_links:
		response = requests.get(params.url)
		soup = BeautifulSoup(response.content,'lxml')
		try:
			classificacao.append(soup.find('div', attrs={'class':'movie-details'}).find_all('span')[1].text)
			trailers.append(soup.find('div', attrs={'class':'movie-details'}).find_all('li')[1].find('a')['href'].replace('//','https://'))
		except:
			classificacao.append(0)
			trailers.append(0)
	if len(classificacao)!= len(movie_names):
		classificacao= classificacao[0:len(movie_names)]

	df = pd.concat([df, pd.DataFrame({'name': movie_names, 'trailers': trailers, 'classificacao': classificacao})])
	df.to_csv(params.raw_data, index=False)

def done(client, params):
	return os.path.isfile(params.raw_data)
	
