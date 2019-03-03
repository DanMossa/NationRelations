import json
import copy
from pathlib import Path

from countries import Countries, get_iso_3, get_all_directed_pairs
from sqlhandler import _SqlHandler


AGGREGATE_JS_DIR = Path("static/aggregates")
COUNTRY_DATA_JS_PATH = Path("static/countryData.js")


sql = _SqlHandler()
COUNTRY_PAIRS = get_all_directed_pairs()


def parse_country_geodata():
    f = open(COUNTRY_DATA_JS_PATH, "r")
    country_js = f.read()
    country_js = country_js.strip()

    country_geo = country_js[country_js.index(" = ") + 3:-1]
    j = json.loads(country_geo)

    return j["features"]
COUNTRY_GEODATA = parse_country_geodata()
def get_geometry_data(country:Countries):
    iso3 = get_iso_3(country)
    for c in COUNTRY_GEODATA:
        if c["id"] is iso3:
            return c["geometry"]
    return None


FEATURE_TEMPLATE = {
    "type": "Feature",
    "id": None,  # 3 character iso code all upper
    "properties": {
        "score": None  # score 0.0 to 1.0 representing sentiment
    },
    "geometry": None
}


class FeatureCollectionBuilder:
    def __init__(self):
        self._main_obj = dict()

    def generate_feature_template(self, objcountry: Countries, home_country: Countries):
        """Takes an in instance of FEATURE_TEMPLATE and the corresponding country"""
        fobj = copy.deepcopy(FEATURE_TEMPLATE)
        fobj["id"] = get_iso_3(objcountry)
        fobj["geometry"] = get_geometry_data(objcountry)
        fobj["properties"]["score"] = sql.get_aggregate_val(objcountry, home_country)[3]

        return fobj

    def generate_collection(self, home_country: Countries):
        js_obj = {
            "type": "FeatureCollection",
            "features": {}
        }
        features = list()
        for c in Countries:
            if c is not home_country:
                features.append(self.generate_feature_template(c, home_country))

        js_obj["features"] = features

        return js_obj

    def get_feature_collection_str(self, focused_country: Countries):
        feature_dict = self.generate_collection(focused_country)
        jstr = json.dumps(feature_dict)

        return jstr


FEATURE_COLLECTION_JS_TEMPLATE = "let {iso3} = {feature_collection_str}"
def generate_feature_collection_files():
    fcb = FeatureCollectionBuilder()
    for c in Countries:
        iso3 = get_iso_3(c)
        feature_collection_str = fcb.get_feature_collection_str(c)
        file_str = FEATURE_COLLECTION_JS_TEMPLATE.format(iso3=iso3, feature_collection_str=feature_collection_str)

        fpath = AGGREGATE_JS_DIR.joinpath(get_iso_3(c) + ".js")
        f = open(fpath, "w+")
        f.write(file_str)
        f.close()


generate_feature_collection_files()
