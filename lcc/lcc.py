import copy


def processBuffer(b, change_log_function):
    b["properties"]["feature_id"] = "Landscape_Conservation_Cooperatives:area_num:{}".format(
        b["properties"]["Area_Num"]
    )
    before_change = copy.deepcopy(b["properties"])

    b["properties"]["feature_name"] = b["properties"]["area_names"]
    b["properties"]["feature_description"] = "null"
    b["properties"]["feature_class"] = "Landscape Conservation Cooperatives"
    b["geometry"]["crs"] = {"type": "name",
                            "properties": {"name": "EPSG:3857"}}

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
