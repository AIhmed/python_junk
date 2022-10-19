import urllib
import pymongo
#conn_str='mongodb+srv://salimongo:'+urllib.parse.quote("S@liM0ng0")+'@cluster0.ka0jl.mongodb.net/sample_supplies?retryWrites=true&w=majority'
#client=pymongo.MongoClient(conn_str,serverSelectionTimeoutMS=10000)
client=pymongo.MongoClient(port=27017)
try:
    db=client.test
    person=db['person']
    for document in person.find({}):
        print(document)
except Exception:
    print("Unable to connect to the server.")
