import datetime
import re

import requests
from bs4 import BeautifulSoup

from rtv.downloader.common import Downloader


class PolsatNewsDL(Downloader):
    _VALID_URL = r'https?://(?:www\.)?polsatnews\.pl/.*'

    def get_podcast_date(self):
        r = requests.get(self.url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        date_str = soup.find('div', class_='article-meta-data').find('div', class_='fl-right').text
        podcast_date = datetime.datetime.strptime(date_str, '%Y-%m-%d, %H:%M')
        return podcast_date

    def get_podcast_show_name(self):
        title_raw = super().get_info().get('title')  # TODO: add error handling if not found (not only here)
        match = re.match(
            r'^.*?-\s*'
            r'(?P<show_name>[\w#\-.,\s]+?)'
            r'\s*-.*$', title_raw)

        # TODO: Fix regex - polsatnews.pl - Prezydenci i premierzy - Jak obywatele odczują zmiany w ustawach sądowych?
        # TODO: czasami po myślniku jest tytuł, do którego trzba dodać regexa, czasami zamiast niego jest tylko data.

        if match:
            return match.group('show_name').replace('-', ' ')

    def get_podcast_title(self):
        # These shows have no title, only show_name and description
        return self.get_podcast_show_name()

    def get_info(self):
        podcast_info = super().get_info()
        self.update_podcast_info_entries(podcast_info, {
            'title': self.get_podcast_title(),
            'show_name': self.get_podcast_show_name(),
            'date': self.get_podcast_date(),
        })
        return podcast_info
