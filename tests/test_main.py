import pytest
from main import calcular_area_triangulo

def test_area_triangulo():
    resultado = calcular_area_triangulo(99, 3)

    assert resultado == pytest.approx(7.5, abs=0.01)