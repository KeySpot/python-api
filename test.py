from src import *

access_key = '60fdb8acb210980ca14738d0'

update_record(access_key, {'new': 'var', 'mumbo': 'jumbo'})

print(get_record(access_key))