class Player:

    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def deck(self):
        return self._deck

    @property
    def is_computer(self):
        return self._is_computer

    def has_empty_deck(self):
        if self._deck.size == 0:
            return True
        else:
            return False

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)