#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: cards.py 
@time: 2020/10/20 15:37 
@desc: 
'''
# code is far away from bugs with the god animal protecting

import collections

# 使用命名元祖
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# beer_card = Card('7', 'diamonds')
# print(beer_card)

deck=FrenchDeck()
# print(len(s))

from random import choice
t=choice(deck)
print(t)

for card in deck:
    print(card)

suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value=FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values)+suit_values[card.suit]

for card in sorted(deck, key=spades_high()):
    print(card)

