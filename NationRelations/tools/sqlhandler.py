import pymysql

from nationrelations.countries import Countries, get_all_directed_pairs


class _SqlHandler:
    _agg_table_name = "aggregate"

    """    _sql_check_table_template = "SELECT * FROM countrydb.tables WHERE table_name = {table_name}"
    _sql_insert_template = "INSERT INTO {table_name} (`TEXT`,`SENTIMENT`,`MAGNITUDE`,`DATE`) VALUES ({text}, {sentiment}, {magnitude}, {date})"
    _sql_get_range_template = "SELECT * FROM '{table_name}' LIMIT {start_index}, {row_count}"
    _sql_get_template = "SELECT * FROM '{table_name}' WHERE ROWNUM={index}"
    _sql_set_aggregate_template = "UPDATE " + _agg_table_name + " SET 'TITLE_SENTEMENT'={new_val} WHERE 'FROM' = '{home_country}' AND 'TO' = {away_country}"
    _sql_get_aggregate_template = "SELECT * FROM " + _agg_table_name + " WHERE 'FROM' = '{home_country}' AND 'TO' = {away_country}"
    """

    def __init__(self):
        self._db = pymysql.connect("localhost", "daniel", "!nation!", "countrydb")
        self._cursor = self._db.cursor()

    def _get_directed_table_name(self, home_country: Countries, away_country: Countries):
        return "{}_to_{}".format(home_country.get_iso_code(), away_country.get_iso_code())

    def table_exists(self, table_name):
        """Checks if a table is present in the database"""
        statement = "SHOW TABLES FROM countrydb LIKE '" + table_name + "'"

        self._cursor.execute(statement)
        result = self._cursor.fetchall()
        if len(result) > 0:
            return True
        return False

    def store_sentiment_data(self, home_country: Countries, away_country: Countries, text, sentiment, magnitude, date):
        tname = self._get_directed_table_name(home_country, away_country)

        # statement = "INSERT INTO {table_name} (`TEXT`,`SENTIMENT`,`MAGNITUDE`,`DATE`) VALUES ({text}, {sentiment}, {magnitude}, {date})".format(
        #     table_name=tname, text=text, sentiment=sentiment, magnitude=magnitude, date=date)

        self._cursor.execute(
            "INSERT INTO `" + tname + "` (`TEXT`,`SENTIMENT`,`MAGNITUDE`,`DATE`) VALUES (%s, %s, %s, %s)",
            (text, sentiment, magnitude, date))
        self._db.commit()

    def get_sentiment_data(self, home_country: Countries, away_country: Countries):
        """Gets a sentiment data point(s)

        :return: returns a list of 4 element tuples
                [
                (text, sentiment, magnitude, date),
                (text, sentiment, magnitude, date),
                (text, sentiment, magnitude, date),
                    ...
                ]
        """
        tname = self._get_directed_table_name(home_country, away_country)
        statement = "SELECT * FROM " + tname
        self._cursor.execute(statement)

        result = self._cursor.fetchall()
        return result

    def set_aggregate_val(self, home_country: Countries, away_country: Countries, new_val):
        """Sets the aggregate value for the specified directed country pair"""
        # statement = "UPDATE " + self._agg_table_name + " SET `title_sentiment`=" + new_val + " WHERE `from`=" + home_country.get_iso_code() + " AND `to`=" + away_country.get_iso_code()
        self._cursor.execute("UPDATE " + self._agg_table_name + " SET `title_sentiment`=%s WHERE `from`=%s AND `to`=%s",
                             (new_val, home_country.get_iso_code(), away_country.get_iso_code()))

        # self._cursor.execute(statement)
        self._db.commit()

    def get_aggregate_val(self, home_country: Countries, away_country: Countries):
        statement = "SELECT * FROM " + self._agg_table_name + " WHERE `from`='" + home_country.get_iso_code() + "' AND `to`='" + away_country.get_iso_code() + "'"

        self._cursor.execute(statement)
        result = self._cursor.fetchall()
        if len(result) == 1:
            return result[0]
        return None
