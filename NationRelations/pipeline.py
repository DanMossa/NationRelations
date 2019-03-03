#!/usr/bin/python3
from countries import get_country_name
from countries import Countries
from analyzer import Analyzer
from sqlhandler import _SqlHandler

class Pipeline:
    def __init__(self):
        self.db_handler = _SqlHandler()
        self.analyzer = Analyzer()
        #List of pairs of Country enums
        self.countries_list = get_all_directed_pairs()

    #RETURNS: tuple of format (SCORE, MAGNITUDE)
    def _analyze_headline(self, headline_text):
        return self.analyzer.getSentiment(headline_text)

    #RETURNS: a list of tuples with format (TEXT, SCORE, MAGNITUDE, DATE)
    #which resembles the records to be stored in the directed SQL tables
    def _compile_directed_country_records(self, headlines_list):
        records_list = list()

        for headline in headlines_list:
            text = headline[0]
            date = headline[1]

            sentiment_tuple = self.analyze_headline(text)
            score = sentiment_tuple[0]
            magnitude = sentiment_tuple[1]

            records_list.append((text, score, magnitude, date))
        return records_list

    def _get_directed_pair_headlines(self, from_country, to_country):
        return get_relevant_headlines(from_country, to_country)

    def compile_all_sentiment_values(self):
        for country_pair in self.countries_list:
            from_country = country_pair[0]
            to_country = country_pair[1]

            headlines_list = self._get_directed_pair_headlines(from_country, to_country)
            records_to_add = self._compile_directed_country_records(headlines_list)
