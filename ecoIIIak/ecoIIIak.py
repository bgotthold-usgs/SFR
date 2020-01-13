import copy


def processBuffer(b, change_log_function):
    b["properties"]["feature_id"] = "Ecoregion_3:us_l3code:{}".format(
        b["properties"]["US_L3CODE"]
    )
    before_change = copy.deepcopy(b["properties"])

    b["properties"]["feature_name"] = b["properties"]["US_L3NAME"]
    b["properties"]["feature_description"] = "null"
    b["properties"]["feature_class"] = "Ecoregion III"
    b["geometry"]["crs"] = {"type": "name",
                            "properties": {"name": "EPSG:5070"}}

    change_log_function(
        b["properties"]["feature_id"],
        'urb/process.py',
        'process',
        "URB Cleanup",
        "Various properties addition/edits",
        before_change,
        b["properties"],
    )
    return b
