from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

    
real_lanche = Restaurante('Real Lanches', 'Hamburgueria')

bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande') 
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 2.00, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
real_lanche.adicionar_no_cardapio(bebida_suco)
real_lanche.adicionar_no_cardapio(prato_pao)




def main():
    real_lanche.exibir_cardapio()



if __name__ == '__main__':
    main()