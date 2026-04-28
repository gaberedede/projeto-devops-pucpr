import pytest
from app import app, somar, subtrair

# fake client para testar 
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# teste 1: para abrir sem dar erro. status 200 = ok
def test_pagina_inicial_abre(client):
    resposta = client.get('/')
    assert resposta.status_code == 200

# teste 2: para ver se o texto  da página esta certo
def test_texto_pagina_inicial(client):
    resposta = client.get('/')
    assert b"API funcionando" in resposta.data

# Teste 3: se a matemática básica de soma funciona
def test_soma_positivos():
    assert somar(2, 3) == 5

# Teste 4: se a soma funciona com números negativos
def test_soma_negativos():
    assert somar(-2, -3) == -5

# Teste 5: se a matemática de subtração funciona
def test_subtracao():
    assert subtrair(10, 4) == 6