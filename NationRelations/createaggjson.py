import json
from pathlib import Path

from countries import Countries, get_iso_3, get_all_directed_pairs
from sqlhandler import _SqlHandler

AGGREGATE_JS_DIR = Path("static/aggregates")

sql = _SqlHandler()
country_pairs = get_all_directed_pairs()


def create_aggregate_json(country: Countries):
    iso3 = get_iso_3(country)
    relevant_pairs = [cp[1] for cp in country_pairs if cp[0] is country]

    aggregate_dict = dict()
    for c in relevant_pairs:
        aggregate_dict[get_iso_3(c)] = sql.get_aggregate_val(country, c)

    json_str = json.dumps(aggregate_dict)
    out_path = AGGREGATE_JS_DIR.joinpath(iso3 + ".json")
    f = open(str(out_path), "w+")
    f.write(json_str)
    f.close()


def create_all_jsons():
    for c in Countries:
        create_aggregate_json(c)


if __name__ == '__main__':
    create_all_jsons()
