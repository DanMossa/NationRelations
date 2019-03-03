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


class CountryAliases(Enum):
    NAME = "name"
    LEADER = "leader"
    CAPITOL = "capitol"


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
    Countries.UNITED_STATES: "United States"
}

_country_3_codes = {
    Countries.ARGENTINA: "ARG",
    Countries.BRAZIL: "BRA",
    Countries.CANADA: "CAN",
    Countries.CHINA: "CHN",
    Countries.CUBA: "CUB",
    Countries.GERMANY: "DEU",
    Countries.HONG_KONG: "HKG",
    Countries.INDIA: "IND",
    Countries.MEXICO: "MEX",
    Countries.RUSSIA: "RUS",
    Countries.UNITED_STATES: "USA"
}

_country_aliases = {
    Countries.ARGENTINA: {
        CountryAliases.NAME: _country_name_map[Countries.ARGENTINA],
        CountryAliases.LEADER: "Mauricio Macri",
        CountryAliases.CAPITOL: "Buenos Aires"
    },
    Countries.BRAZIL: {
        CountryAliases.NAME: _country_name_map[Countries.BRAZIL],
        CountryAliases.LEADER: "Jair Bolsonaro",
        CountryAliases.CAPITOL: "Brasília"
    },
    Countries.CANADA: {
        CountryAliases.NAME: _country_name_map[Countries.CANADA],
        CountryAliases.LEADER: "Justin Trudeau",
        CountryAliases.CAPITOL: "Ottawa"
    },
    Countries.CHINA: {
        CountryAliases.NAME: _country_name_map[Countries.CHINA],
        CountryAliases.LEADER: "Xi Jinping",
        CountryAliases.CAPITOL: "Beijing"
    },
    Countries.CUBA: {
        CountryAliases.NAME: _country_name_map[Countries.CUBA],
        CountryAliases.LEADER: "Miguel Díaz-Canel",
        CountryAliases.CAPITOL: "Havana"
    },
    Countries.GERMANY: {
        CountryAliases.NAME: _country_name_map[Countries.GERMANY],
        CountryAliases.LEADER: "Frank-Walter Steinmeier",
        CountryAliases.CAPITOL: "Berlin"
    },
    Countries.HONG_KONG: {
        CountryAliases.NAME: _country_name_map[Countries.HONG_KONG],
        CountryAliases.LEADER: "Carrie Lam",
        CountryAliases.CAPITOL: "Hong Kong central"
    },
    Countries.INDIA: {
        CountryAliases.NAME: _country_name_map[Countries.INDIA],
        CountryAliases.LEADER: "Ram Nath Kovind",
        CountryAliases.CAPITOL: "New Delhi"
    },
    Countries.MEXICO: {
        CountryAliases.NAME: _country_name_map[Countries.MEXICO],
        CountryAliases.LEADER: "Andrés Manuel López Obrador",
        CountryAliases.CAPITOL: "Mexico City"
    },
    Countries.RUSSIA: {
        CountryAliases.NAME: _country_name_map[Countries.RUSSIA],
        CountryAliases.LEADER: "Vladimir Putin",
        CountryAliases.CAPITOL: "Moscow"
    },
    Countries.UNITED_STATES: {
        CountryAliases.NAME: _country_name_map[Countries.UNITED_STATES],
        CountryAliases.LEADER: "Donald Trump",
        CountryAliases.CAPITOL: "Washington D.C."
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


def get_country_alias(country: Countries, alias_type: CountryAliases):
    """Gets the alias for the specified country and alias type"""
    if country in _country_aliases:
        target_country = _country_aliases[country]
        if alias_type in target_country.keys():
            return target_country[alias_type]
    return None


def get_all_directed_pairs():
    country_pairs = list()
    for fromc in Countries:
        for toc in Countries:
            if fromc != toc:
                country_pairs.append((fromc, toc))
    return country_pairs


def get_iso_3(country: Countries):
    """Gets 3 digit ISO country code"""
    if country in _country_3_codes.keys():
        return _country_3_codes[country]
    return ""


if __name__ == '__main__':
    pairs = get_all_directed_pairs()
    for p in pairs:
        print(p)
    print(len(pairs))
