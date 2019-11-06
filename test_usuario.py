from src.leilao.dominio import Usuario, Leilao, LanceInvalido
import pytest


@pytest.fixture
def eurico():
  return Usuario('eurico', 100.0)

@pytest.fixture
def leilao():
  return Leilao('celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(eurico, leilao):
  

  eurico.propoe_lance(leilao, 50.0)

  assert eurico.carteira == 50.0

def test_deve_permitir_propor_lance_quando_valor_menor_do_que_saldo_na_carteira(eurico, leilao):
  

  eurico.propoe_lance(leilao, 1.0)

  assert eurico.carteira == 99.0

def test_deve_permitir_propor_lance_quando_valor_e_igual_ao_saldo_na_carteira(eurico, leilao):
  

  eurico.propoe_lance(leilao, 100.0)

  assert eurico.carteira == 0

def test_nao_deve_permitir_propor_lance_com_valor_superior_ao_saldo_da_carteira(eurico, leilao):
  with pytest.raises(LanceInvalido):

    

    eurico.propoe_lance(leilao, 200.0)
