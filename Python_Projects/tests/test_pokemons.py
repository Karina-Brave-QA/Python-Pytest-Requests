import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'accf014adbbef322a5b1b17c62bea6d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4043'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID } )
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID } )
    assert response_get.json()["data"][0]["trainer_id"] == TRAINER_ID


@pytest.mark.parametrize('key, value' , [('name','Бульбазавр'),('trainer_id', TRAINER_ID ),('id', '26884')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID } )
    assert response_parametrize.json()["data"][0][key] == value 