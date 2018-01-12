import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json

schema = avro.schema.parse(open("tweets.avsc", "rb").read())

writer = DataFileWriter(open("tweets.avro", "wb"), DatumWriter(), schema)

writer.append({"username":"VoidRay","tweet":"Prismatic core online!","timestamp":1366160000})
writer.append({"username":"DarkTemplar","tweet":"Prismatic core online1","timestamp":1366154681})
writer.append({"username":"BlizzardCS","tweet":"Prismatic core online2","timestamp":1366154481})
# writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("tweets.avro", "rb"), DatumReader())
for user in reader:
    print user
reader.close()