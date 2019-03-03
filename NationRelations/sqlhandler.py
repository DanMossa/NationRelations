import pymysql

from countries import Countries


class _SqlHandler:
    _agg_table_name = "aggregate"

    _sql_insert_template = "INSERT INTO '{table_name}' VALUES ({text}, {sentiment}, {magnitude}, {date})"
    _sql_check_table_template = "SELECT * FROM countrydb.tables WHERE table_name = {table_name}"
    _sql_set_aggregate_template = "UPDATE aggregate SET 'TITLE_SENTEMENT'={new_val} WHERE 'FROM' = '{home_country}' AND 'TO' = {away_country}"
    _sql_get_aggregate_template = "SELECT * FROM " + _agg_table_name + " WHERE 'FROM' = '{home_country}' AND 'TO' = {away_country}"

    def __init__(self):
        self._db = pymysql.connect("localhost", "daniel", "!nation!", "countrydb")
        self._cursor = self._db.cursor()

    def _get_directed_table_name(self, home_country: Countries, away_country: Countries):
        return "{}_to_{}".format(home_country.get_iso_code(), away_country.get_iso_code())

    def table_exists(self, table_name):
        """Checks if a table is present in the database"""
        statement = self._sql_check_table_template.format(table_name=table_name)
        self._cursor.execute(statement)
        result = self._cursor.fetchall()
        if len(result) > 0:
            return True
        return False

    def store_sentiment_data(self, home_country: Countries, away_country: Countries, text, sentiment, magnitude, date):
        tname = self._get_directed_table_name(home_country, away_country)
        statement = self._sql_insert_template.format(table_name=tname, text=text, sentiment=sentiment, magnitude=magnitude, date=date)

        self._cursor.execute(statement)
        self._db.commit()

    def get_sentiment_data(self, home_country: Countries, away_country: Countries, row):
        """Gets a single sentiment

        :param home_country:
        :param away_country:
        :param row: either an int to get a single row, or a range in form (int, int)
        :return:
        """
        pass

    def set_aggregate_val(self, home_country: Countries, away_country: Countries, new_val):
        """Sets the aggregate value for the specified directed country pair"""
        statement = self._sql_set_aggregate_template.format(new_val=new_val, home_country=home_country.get_iso_code(), away_country=away_country.get_iso_code())

        self._cursor.execute(statement)
        self._db.commit()

    def get_aggregate_val(self, home_country: Countries, away_country: Countries):
        statement = self._sql_get_aggregate_template.format(home_country=home_country.get_iso_code(), away_country=away_country.get_iso_code())

        self._cursor.execute(statement)
        result = self._cursor.fetchall()
        if len(result) == 1:
            return result[0]
        return None
