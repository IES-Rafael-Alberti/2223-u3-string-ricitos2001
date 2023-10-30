import pytest
from src.actividad4 import crear_cuenta
@pytest.mark.parametrize(
    "palabra, caracter, cuenta",
    [
        ("hola mundo me llamo cesar","a",3)
    ]
)
def test_crear_cuenta_params(palabra,caracter,cuenta):
    assert crear_cuenta(palabra,caracter)==cuenta