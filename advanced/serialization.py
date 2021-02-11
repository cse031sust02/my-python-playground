# Serialization
# ==============
# When transmitting data or storing them in a file, the data are required to be
# byte strings, but complex objects are seldom in this format. Serialization can
# convert these complex objects into byte strings for such use. After the byte
# strings are transmitted, the receiver will have to recover the original object
# from the byte string. This is known as deserialization.
# src : https://stackoverflow.com/a/3316779
 
# To serialize and de-serialize a Python object, there are various ways.

data = {
    "student": {
        "name": "John Doe",
        "dept": "CSE",
        "id": 'A0001',
        "scholarship": True,
    }
}

# JSON
# ======
# Using json, we can convert a Python object into a JSON format and vice versa.

import json

json_data = json.dumps(data)  # serialize
print(type(json_data), " : ", json_data)

python_data = json.loads(json_data)  # deserialize
print(type(python_data), " : ", python_data)

# Pickle
# ========
# Using pickle, we can convert a Python object into a byte stream and vice versa.

import pickle

byte_data = pickle.dumps(data) # serialize
print(type(byte_data), " : ", byte_data)

python_dict = pickle.loads(byte_data) # deserialize
print(type(python_dict), " : ", python_dict)
