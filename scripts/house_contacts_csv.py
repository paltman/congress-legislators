import csv

import rtyaml


def convert():
    data = rtyaml.load(open("legislators-current.yaml", "rb"))
    reps = [x for x in data if x["terms"][-1]["type"] == "rep"]
    fields = [
        "official_full",
        "first",
        "middle",
        "last",
        "birthday",
        "gender",
        "start",
        "end",
        "state",
        "district",
        "party"
    ]
    with open("legislators-current.csv", "wb") as fp:
        writer = csv.DictWriter(fp, fields)
        writer.writeheader()
        rep_data = {}
        for rep in reps:
            rep_data["official_full"] = rep["name"]["official_full"].encode("utf-8")
            rep_data["first"] = rep["name"]["first"].encode("utf-8")
            rep_data["middle"] = rep["name"].get("middle", "").encode("utf-8")
            rep_data["last"] = rep["name"]["last"].encode("utf-8")
            rep_data["birthday"] = rep["bio"]["birthday"]
            rep_data["gender"] = rep["bio"]["gender"]
            rep_data["start"] = rep["terms"][-1]["start"]
            rep_data["end"] = rep["terms"][-1]["end"]
            rep_data["state"] = rep["terms"][-1]["state"]
            rep_data["district"] = rep["terms"][-1]["district"]
            rep_data["party"] = rep["terms"][-1]["party"]
            writer.writerow(rep_data)


if __name__ == "__main__":
    convert()
