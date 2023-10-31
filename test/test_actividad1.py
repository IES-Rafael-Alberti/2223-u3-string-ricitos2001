import pytest
from src.actividad1 import crear_lista
@pytest.mark.parametrize(
    "palabra,letras",
    [
        ("hola",["a","l","o","h"])
    ]
)
def test_crear_lista_params(palabra,letras):
    assert crear_lista(palabra)==letras