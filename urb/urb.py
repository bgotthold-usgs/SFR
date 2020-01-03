import copy


def processBuffer(b, change_log_function):
    b["properties"]["feature_id"] = "Unified_Regions:id:{}".format(
        b["properties"]["REG_NUM"]
    )
    before_change = copy.deepcopy(b["properties"])

    b["properties"]["feature_name"] = b["properties"]["REG_NAME"]
    b["properties"]["feature_description"] = "null"
    b["properties"]["feature_class"] = "Unified Regions"
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
