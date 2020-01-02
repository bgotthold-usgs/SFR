
import os
import json
from urb.urb import *

json_schema = None


def process_1(
    path,
    file_name,
    ch_ledger,
    send_final_result,
    send_to_send_to_stage,
    previous_stage_result,
):
    count = 0

    file_name = file_name.split(".")[0]  # remove the .zip if applicable
    buffer = getGeoJsonFromShapefile(path + file_name)


    for b in buffer:

        b["properties"]["feature_id"] = "US_States_and_Territories:state_fipscode:{}".format(
            b["properties"]["STATEFP"]
        )
        before_change = copy.deepcopy(b["properties"])

        b["properties"]["feature_name"] = b["properties"]["NAME"]
        b["properties"]["feature_description"] = "null"
        b["properties"]["feature_class"] = "US States and Territories"
        b["geometry"]["crs"] = {"type":"name","properties":{"name":"EPSG:3857"}}

        ch_ledger.log_change_event(
            b["properties"]["feature_id"],
            'urb/process.py',
            'process',
            "URB Cleanup",
            "Various properties addition/edits",
            before_change,
            b["properties"],
        )

        r = get_json_doc(b)
        send_final_result(r)
        count += 1

    return count
