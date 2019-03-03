import json
import datetime

from eventregistry import EventRegistry, QueryArticles, QueryItems, ComplexArticleQuery

from countries import Countries, CountryAliases, get_country_alias, get_country_language

# Init
_api = EventRegistry(apiKey=json.load(open("NationRelations/res/keys.json", 'r'))["news"])
_location_uris = {c: _api.getLocationUri(get_country_alias(c, CountryAliases.NAME)) for c in Countries}


def _get_month_ago():
    """Gets the date a month ago in the format accepted by EvnetRegistry

    returns in form YYYY-MM-DD
    """
    d = datetime.date.today()
    ddelta = datetime.timedelta(days=31)
    return str(d - ddelta)


def get_relevant_headlines(home_country: Countries, target_country: Countries):
    """Pulls article headlines and creation dates from the EventRegistry API

    :returns [
        (<Article title>, <Article date create>),
        (<Article title>, <Article date create>),
        (<Article title>, <Article date create>),
        ...
        ]
    """
    target_aliases = [
        get_country_alias(target_country, CountryAliases.NAME),
        get_country_alias(target_country, CountryAliases.CAPITOL),
        get_country_alias(target_country, CountryAliases.LEADER)
    ]
    qparams = {
        "keywords": QueryItems.OR(target_aliases),
        "sourceLocationUri": _location_uris[home_country],
        "dateStart": _get_month_ago(),
        "keywordsLoc": "body,title",
        "isDuplicateFilter": "keepOnlyDuplicates",
        "dataType": ["news", "pr"]
    }
    query = QueryArticles(**qparams)
    result = _api.execQuery(query)["articles"]["results"]

    to_return = list()
    for a in result:
        relevant = (a["title"], a["date"])
        to_return.append(relevant)
    return to_return


if __name__ == '__main__':
    heads = get_relevant_headlines(Countries.UNITED_STATES, Countries.RUSSIA)
    for i in heads:
        print(i)
