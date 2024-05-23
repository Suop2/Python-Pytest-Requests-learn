import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '954873526f2f2abfc9dbaef95be4ce1c'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token':'954873526f2f2abfc9dbaef95be4ce1c'
          }
HEADER_CHANGENAME = {'Content-Type' : 'application/json'}
BODY_POKEMON_ID = {
    "pokemon_id": "28086"
}
body_pokemons = {
    "name": "Wesper",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_changename = {
    "pokemon_id": "28086",
    "name": "Wesper",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_pokemons)
print(response.text)

#response_changename = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_changename)
#print(response_changename.text)

#response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEMON_ID)
#print(response_add_pokeball.text)