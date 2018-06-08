"""File that scrap IMDB website."""

import requests  # to connect to web pages
from bs4 import BeautifulSoup  # to extract information from html
import pandas as pd  # to manipulate data and export to csv format


def get_synopsis(soup):
    """Get synopsis."""
    synopsis = soup.find('div', attrs={'class': 'summary_text'})
    if synopsis.text:
        return synopsis.text
    else:
        return None


def get_director(soup):
    """Get director info."""
    director = soup.find('span', attrs={'class': 'itemprop'}, itemprop='name')
    if director.text:
        return director.text
    else:
        return None


def get_genre(soup):
    """Get genre info."""
    genre = soup.find('div', attrs={'class': 'see-more inline canwrap'}, itemprop='genre')
    if genre is not None:
        return [a.text for a in genre.findAll('a')]
    else:
        return None


def get_country(soup):
    """Get country info."""
    country_tags = soup.select("a[href*=country_of_origin]")
    if len(country_tags) > 0:
        return [c.text for c in country_tags]
    else:
        return None


def get_idiom(soup):
    """Get idiom info."""
    language_tags = soup.select("a[href*=primary_language]")
    if len(language_tags) > 0:
        return language_tags[0].text
    else:
        return None


def get_duration(soup):
    """Get duration info."""
    pass


def get_score(soup):
    """Get movie score info."""
    pass


def get_title(soup):
    """Get movie title."""
    pass


def get_production_year(soup):
    """Get production movie year."""
    pass


def get_qtd_review(soup):
    """Get quantity of reviews."""
    pass


url_fonte = "http://www.imdb.com/find?q=Christmas&s=tt&ref_=fn_tt"
# url_movie = "http://www.imdb.com/title/tt1260564/?ref_=fn_tt_tt_200"
url_movie = "http://www.imdb.com/title/tt1410207/?ref_=fn_tt_tt_1"

print(url_movie)
con = requests.get(url_movie)
print(con.status_code)

# create BeautifulSoup object with the html page
soup = BeautifulSoup(con.content, "html.parser")
# print(soup.prettify())

# titulos_filmes = [tag.find('a').contents[0] for tag in soup.findAll('td', attrs={'class':'result_text'})]
# print(titulos_filmes)

# movies_links = ['http://www.imdb.com' + tag.a['href']  for tag in soup.findAll('td', attrs={'class':'result_text'})]
# print(movies_links)
synopsis = get_synopsis(soup)
print(synopsis)

director = get_director(soup)
print(director)

genre = get_genre(soup)
print(genre)

country = get_country(soup)
print(country)

idiom = get_idiom(soup)
print(idiom)
