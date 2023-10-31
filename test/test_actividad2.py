import pytest
from src.actividad2 import crear_fruta
@pytest.mark.parametrize(
    "listafruta,fruta",
    [
        ("fruta","fruta")
    ]
)
def test_crear_fruta_params(listafruta,fruta):
    assert crear_fruta(listafruta)==fruta