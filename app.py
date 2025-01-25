from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

    
real_lanche = Restaurante('Real Lanches', 'Hamburgueria')

bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande') 
prato_pao = Prato('Pão', 2.00, 'O melhor pão da cidade')




def main():
    print(prato_pao)
    print(bebida_suco)



if __name__ == '__main__':
    main()