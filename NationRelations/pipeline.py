#!/usr/bin/python3
from countries import get_country_name, Countries, get_all_directed_pairs
from news import get_relevant_headlines
from sqlhandler import _SqlHandler
from analyzer import Analyzer

class Pipeline:
    def __init__(self):
        self.database = _SqlHandler()
        self.analyzer = Analyzer()
        #List of pairs of Country enums
        self.countries_list = get_all_directed_pairs()

    #RETURNS: tuple of format (SCORE, MAGNITUDE)
    def _analyze_headline(self, headline_text):
        return self.analyzer.getSentiment(headline_text)

    def __get_records(self, from_country: Countries, to_country: Countries):
        results = self.database.get_sentiment_data(from_country, to_country)
        return results

    def __compute(self, records_list):
        summation = 0
        if records_list is None:
            return
        for record in records_list:
            print(record)
            score = record[2]
            summation += score
        return (summation / len(records_list))

    #RETURNS: a list of tuples with format (TEXT, SCORE, MAGNITUDE, DATE)
    #which resembles the records to be stored in the directed SQL tables
    def __generate_directed_country_records(self, headlines_list):
        records_list = list()

        for headline in headlines_list:
            text = headline[0]
            date = headline[1]

            sentiment_tuple = self._analyze_headline(text)
            score = sentiment_tuple[0]
            magnitude = sentiment_tuple[1]

            records_list.append((text, score, magnitude, date))
        return records_list

    def _get_directed_pair_headlines(self, from_country: Countries, to_country: Countries):
        return get_relevant_headlines(from_country, to_country)

    def _write_to_directed_table(self, from_country: Countries, to_country: Countries, record_tuple):
        self.database.store_sentiment_data(from_country, to_country, *record_tuple)

    def _write_to_aggregate_table(self, from_country: Countries, to_country: Countries, value):
        self.database.set_aggregate_val(from_country, to_country, value)

    #Takes the list of directed country pairs, retrieves the related headlines,
    #creates record-format tuples, then writes them to the database
    def process_directed_country_data(self):
        for country_pair in self.countries_list:
            from_country = country_pair[0]
            to_country = country_pair[1]

            headlines_list = self._get_directed_pair_headlines(from_country, to_country)
            records_to_add = self.__generate_directed_country_records(headlines_list)

            for record in records_to_add:
                self._write_to_directed_table(from_country, to_country, record)

    def compute_aggregate_score(self, from_country: Countries, to_country: Countries):
        records_list = list()
        limit = 100

        records_list = self.__get_records(from_country, to_country)

        new_score = self.__compute(records_list)
        print(new_score)
        self._write_to_aggregate_table(from_country, to_country, new_score)

    def compute_all_aggregate_scores(self):
        for country_pair in self.countries_list:
            from_country = country_pair[0]
            to_country = country_pair[1]

            records_list = self.__get_records(from_country, to_country)

            new_score = self.__compute(records_list)
            print(type(new_score))
            self._write_to_aggregate_table(from_country, to_country, new_score)
