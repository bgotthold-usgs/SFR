
import os
import json
from ecoIIIak.ecoIIIak import processBuffer
from resources.shapefile_helper import getGeoJsonFromShapefile, get_json_doc

json_schema = None
try:
    with open(os.path.join(os.path.dirname(__file__), './SFR_schema.json'), 'r') as json_schema_file:
        json_schema = json.load(json_schema_file)
except FileNotFoundError as e:
    pass


def process_1(
    path,
    ch_ledger,
    send_final_result,
    send_to_send_to_stage,
    previous_stage_result,
):
    count = 0
    buffer = getGeoJsonFromShapefile(path)
    for b in buffer:
        data = processBuffer(b, change_log_function=ch_ledger.log_change_event)
        result = get_json_doc(data)
        send_final_result(result)
        count += 1

    return count

