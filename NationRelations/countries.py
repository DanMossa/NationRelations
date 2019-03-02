from enum import Enum


class Countries(Enum):
    """ISO 3166-1 country codes available in News API"""
    ARGENTINA = "ar"
    BRAZIL = "br"
    CANADA = "ca"
    CHINA = "cn"
    CUBA = "cu"
    GERMANY = "de"
    HONG_KONG = "hk"
    INDIA = "in"
    MEXICO = "mx"
    RUSSIA = "ru"
    UNITED_STATES = "us"

    def get_iso_code(self):
        """Returns the corresponding 2 char ISO 3166-1 code"""
        return self.value

    def __str__(self):
        return self.value


class Languages(Enum):
    """ISO 639-1 codes available in News API"""
    ARABIC = "ar"
    GERMAN = "de"
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    HEBREW = "he"
    ITALIAN = "it"
    DUTCH = "nl"
    NORWEGIAN = "no"
    PORTUGESE = "pt"
    RUSSIAN = "ru"
    URALIC = "se"
    CHINESE = "zh"

    def get_iso_code(self):
        return self.value

    def __str__(self):
        return self.value


_country_lang_map = {
    Countries.ARGENTINA: Languages.SPANISH,
    Countries.BRAZIL: Languages.PORTUGESE,
    Countries.CANADA: Languages.ENGLISH,
    Countries.CHINA: Languages.CHINESE,
    Countries.CUBA: Languages.SPANISH,
    Countries.GERMANY: Languages.GERMAN,
    Countries.HONG_KONG: Languages.CHINESE,
    Countries.INDIA: Languages.ENGLISH,
    Countries.MEXICO: Languages.SPANISH,
    Countries.RUSSIA: Languages.RUSSIAN,
    Countries.UNITED_STATES: Languages.ENGLISH
}


_country_name_map = {
    Countries.ARGENTINA: "Argentina",
    Countries.BRAZIL: "Brazil",
    Countries.CANADA: "Canada",
    Countries.CHINA: "China",
    Countries.CUBA: "Cuba",
    Countries.GERMANY: "Germany",
    Countries.HONG_KONG: "Hong Kong",
    Countries.INDIA: "India",
    Countries.MEXICO: "Mexico",
    Countries.RUSSIA: "Russia",
    Countries.UNITED_STATES: "United State of America"
}


_country_aliases = {
    Countries.ARGENTINA: {
        "name": _country_name_map[Countries.ARGENTINA],
        "leader": "Mauricio Macri",
        "capitol": "Buenos Aires"
    },
    Countries.BRAZIL: {
        "name": _country_name_map[Countries.BRAZIL],
        "leader": "Jair Bolsonaro",
        "capitol": "Brasília"
    },
    Countries.CANADA: {
        "name": _country_name_map[Countries.CANADA],
        "leader": "Justin Trudeau",
        "capitol": "Ottawa"
    },
    Countries.CHINA: {
        "name": _country_name_map[Countries.CHINA],
        "leader": "Xi Jinping",
        "capitol": "Beijing"
    },
    Countries.CUBA: {
        "name": _country_name_map[Countries.CUBA],
        "leader": "Miguel Díaz-Canel",
        "capitol": "Havana"
    },
    Countries.GERMANY: {
        "name": _country_name_map[Countries.GERMANY],
        "leader": "Frank-Walter Steinmeier",
        "capitol": "Berlin"
    },
    Countries.HONG_KONG: {
        "name": _country_name_map[Countries.HONG_KONG],
        "leader": "Carrie Lam",
        "capitol": "Hong Kong central"
    },
    Countries.INDIA: {
        "name": _country_name_map[Countries.INDIA],
        "leader": "Ram Nath Kovind",
        "capitol": "New Delhi"
    },
    Countries.MEXICO: {
        "name": _country_name_map[Countries.MEXICO],
        "leader": "Andrés Manuel López Obrador",
        "capitol": "Mexico City"
    },
    Countries.RUSSIA: {
        "name": _country_name_map[Countries.RUSSIA],
        "leader": "Vladimir Putin",
        "capitol": "Moscow"
    },
    Countries.UNITED_STATES: {
        "name": _country_name_map[Countries.UNITED_STATES],
        "leader": "Donald Trump",
        "capitol": "Washington D.C."
    }
}


def get_country_language(country: Countries):
    if country in _country_lang_map.keys():
        return _country_lang_map[country]
    return None


def get_country_name(country: Countries):
    if country in _country_name_map.keys():
        return _country_name_map[country]
    return None

