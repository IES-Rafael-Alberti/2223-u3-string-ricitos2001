import pytest
from src.actividad3 import crear_cuenta
@pytest.mark.parametrize(
    "palabra,caracter,cuenta",
    [
        ("banana","a",3)
    ]
)
def test_crear_cuenta_params(palabra,caracter,cuenta):
    assert crear_cuenta(palabra,caracter)==cuenta