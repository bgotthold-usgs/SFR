import copy


def processBuffer(b, change_log_function):
    b["properties"]["feature_id"] = "US_States_and_Territories:state_fipscode:{}".format(
        b["properties"]["STATEFP"]
    )
    before_change = copy.deepcopy(b["properties"])

    b["properties"]["feature_name"] = b["properties"]["NAME"]
    b["properties"]["feature_description"] = "null"
    b["properties"]["feature_class"] = "US States and Territories"
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
