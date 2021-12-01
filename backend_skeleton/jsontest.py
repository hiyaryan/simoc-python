import json
json_format_file = "step_data.json"
# Load the format file to save from
with open(json_format_file, ) as file:
    sensor_json = json.load(file)

with open(json_format_file, ) as file:
    next_json=json.load(file)

next_json[0]["id"]="XXXX"
sensor_json.append(next_json[0])


with open(json_format_file, ) as file:
    next_json=json.load(file)
    next_json[0]["step_num"]=222222222
    next_json[0]["storage_capacities"]["air_storage"]["1"]["atmo_co2"]["value"]=999999999999999999999999;
    next_json[0]["storage_capacities"]["air_storage"]["1"]["atmo_h2o"]["value"]=777777777777777777777777;
    next_json[0]["total_production"]["atmo_co2"]["value"]=333333333333333333333333333333333;
    next_json[0]["total_consumption"]["atmo_co2"]["value"]=-111111111111111111111111111111;
next_json[0]["id"]="YYYY"
small_object = {"222222222":0}
small_object["222222222"] = next_json[0]["storage_capacities"]["air_storage"].pop("1")
next_json[0]["storage_capacities"]["air_storage"]=small_object;
small_object = {"222222222":0}
small_object["222222222"] = next_json[0]["storage_capacities"]["water_storage"].pop("1")
next_json[0]["storage_capacities"]["water_storage"]=small_object;
small_object = {"222222222":0}
small_object["222222222"] = next_json[0]["storage_capacities"]["nutrient_storage"].pop("1")
next_json[0]["storage_capacities"]["nutrient_storage"]=small_object;
small_object = {"222222222":0}
small_object["222222222"] = next_json[0]["storage_capacities"]["power_storage"].pop("1")
next_json[0]["storage_capacities"]["power_storage"]=small_object;
small_object = {"222222222":0}
small_object["222222222"] = next_json[0]["storage_capacities"]["food_storage"].pop("1")
next_json[0]["storage_capacities"]["food_storage"]=small_object;
sensor_json.append(next_json[0])

print(small_object)
print(sensor_json)
