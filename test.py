from src import keyspot

access_key = '610ee66604b4af8d1b15d740'

update_record(access_key, {'new': 'var', 'mumbo': 'jumbo'})

print(get_record(access_key))