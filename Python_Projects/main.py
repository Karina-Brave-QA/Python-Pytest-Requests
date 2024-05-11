import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'accf014adbbef322a5b1b17c62bea6d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '26879'
body_registration = {
    "trainer_token": TOKEN,
    "email": "karinakhrabraya@gmail.com",
    "password": "Iloveqa1"
}

body_cofirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change_pokemon = {
    "pokemon_id": POKEMON_ID,
    "name": "Nme",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_kill = {
    "pokemon_id": POKEMON_ID
}

body_add_pokeball = {
    "pokemon_id": POKEMON_ID
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email' , headers = HEADER, json = body_cofirmation )
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change_pokemon = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_change_pokemon )
print(response_change_pokemon.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_add_pokeball )
print(response_add_pokeball.text)

'''response_kill = requests.post(url = f'{URL}/pokemons/knockout' , headers = HEADER, json = body_kill )
print(response_kill.text)'''