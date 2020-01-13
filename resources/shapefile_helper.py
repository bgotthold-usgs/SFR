
import shapefile
import glob

def getGeoJsonFromShapefile(path):
    # read the shapefile
    myshp = open(glob.glob("{}*.shp".format(path))[0], "rb")
    mydbf = open(glob.glob("{}*.dbf".format(path))[0], "rb")
    reader = shapefile.Reader(shp=myshp, dbf=mydbf)

    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", geometry=geom, properties=atr))
    return buffer

def get_json_doc(data):
    return {
        "data": {
            "feature_id": data["properties"]["feature_id"],
            "feature_name": data["properties"]["feature_name"],
            "feature_description": data["properties"]["feature_description"],
            "feature_class": data["properties"]["feature_class"],
        },
        "row_id": data["properties"]["feature_id"],
        "geometry":  data["geometry"]
    }