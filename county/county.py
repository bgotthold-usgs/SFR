import copy


def processBuffer(b, change_log_function):
    b["properties"]["feature_id"] = "US County:county:{}".format(
        b["properties"]["STATEFP"],b["properties"]["COUNTYFP"]
    )
    before_change = copy.deepcopy(b["properties"])

    b["properties"]["feature_name"] = b["properties"]["NAME"]
    b["properties"]["feature_description"] = "null"
    b["properties"]["feature_class"] = "US County"
    b["geometry"]["crs"] = {"type": "name",
                            "properties": {"name": "EPSG:3857"}}

    change_log_function(
        b["properties"]["feature_id"],
        'county/process.py',
        'process',
        "County Cleanup",
        "Various properties addition/edits",
        before_change,
        b["properties"],
    )
    return b