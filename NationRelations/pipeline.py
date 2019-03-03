#!/usr/bin/python3
import pymysql
import countries
from countries import Countries
from analysis import Analysis

class Pipeline:
    def __init__(self):
        self.db = pymysql.connect("localhost","daniel","!nation!","countrydb" )
        self.analyzer = Analyzer()

    def _queryNews(self, Countries: ):
