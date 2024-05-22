import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '44a029af93de8aba28770d02e8379fd8'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2364'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['name'] =='Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id','28060')])
def test_parametrize(key, value):
    response_param = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_param.json()['data'][0][key] == value