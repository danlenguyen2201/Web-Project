import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds131384.mlab.com:31384/warmwinter

host = "ds131384.mlab.com"
port = 31384
db_name = "warmwinter"
user_name = "DemonLordXD"
password = "Dankeo123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
