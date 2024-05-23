import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '954873526f2f2abfc9dbaef95be4ce1c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2287'

def test_code_status():
    response  = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name_check():
    response_get = requests.get(url=f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["trainer_name"] == 'серж'   

