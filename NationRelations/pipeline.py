#!/usr/bin/python3
import pymysql
import countries
from countries import Countries
from analysis import Analysis

class Pipeline:
    def __init__(self):
        self.db = pymysql.connect("localhost","daniel","!nation!","countrydb" )
        self.analyzer = Analyzer()
        self.countries_list = get_all_directed_pairs()

    def _insertToTable(self);


    def updateDirectedTables(self):
        for countryPair in self.countries_list:
            fromCountry = countryPair[0]
            toCountry = countryPair[1]
            headlines = get_relevant_headlines(fromCountry, toCountry)

            for headline in headlines:
                text = headline[0]
                date = headline[1]
