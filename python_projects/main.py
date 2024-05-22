import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '44a029af93de8aba28770d02e8379fd8'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_make_pokemons = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_of_change = {
    "pokemon_id": "28056",
    "name": "Сафушкин",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add = {
    "pokemon_id": "28055"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_make_pokemons)
print(response.text)
print(response.status_code)

message = response.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_of_change)
print(response_change.status_code)

message = response_change.json()['message']
print(message)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add_pokeball.status_code)

message = response_add_pokeball.json()['message']
print(message)