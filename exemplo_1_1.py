# Um baralho com uma sequência de cartas

import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
        
    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> str:
        return self._cards[position]
    
##################################################################################

#Representação da namedtuple
beer_card = Card('7', 'diamonds')
print(beer_card)

# Número de cartas do baralho
deck = FrenchDeck()
print(len(deck))

# Utilizando o método __getitem__
print(deck[0]) # 1º Pos
print(deck[-1]) #Última Pos

#Selecionar cartas aleatórias 
from random import choice
print(choice(deck))

# fatiamento(slicing)

print(f"Os 3 primeiros: {deck[:3]}\n")
print(f"Os elementos da sequência original {deck[12::13]}\n")

#Interações
for card in deck:
    print(card)

print("\n **************************************************** \n")
for card in reversed(deck): #Ordem inversa
    print(card)

print("\n ***************************************** \n")

#Verificações
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)


#Ordenação
print("\n ***************************************** \n")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs = 0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)