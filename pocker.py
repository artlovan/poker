#!/usr/bin/env python

"""
Code will:
- Code handles case where there is only one player but player_id is not 0 (e.g. id's aren't assigned incrementally)
- ValueError is raised if n is not a number (e.g. whole number / integer)
- AssertionError is raised if n results in False for 0 < n < 24
- AssertionError is raised if suite is other then in ['h', 'd', 's', 'c']
- AssertionError is raised if rank is other then in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
- IndexError is raised if two players have same card (two players can't have exactly same card in same game)
- ValueError is raised if multiple players have same id
- AssertionError is raised if n is not equal (e.g. is less or grater) to number of players
- ValueError is raised if the card is not valid
  Valid cards are:
    ['2h', '2d', '2s', '2c',
    '3h', '3d', '3s', '3c',
    '4h', '4d', '4s', '4c',
    '5h', '5d', '5s', '5c',
    '6h', '6d', '6s', '6c',
    '7h', '7d', '7s', '7c',
    '8h', '8d', '8s', '8c',
    '9h', '9d', '9s', '9c',
    'Th', 'Td', 'Ts', 'Tc',
    'Jh', 'Jd', 'Js', 'Jc',
    'Qh', 'Qd', 'Qs', 'Qc',
    'Kh', 'Kd', 'Ks', 'Kc',
    'Ah', 'Ad', 'As', 'Ac']
"""


RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITE = ['h', 'd', 's', 'c']


def assert_unique_id(id, registered_ids):
    if id in registered_ids:
        raise ValueError("Multiple players can't have same id {}".format(str(id)))
    registered_ids.append(id)
    return id


def get_game_cards():
    cards = []
    [cards.append('{}{}'.format(r, s)) for r in RANKS for s in SUITE]
    return cards


def assert_suite(card):
    card_array = list(card)
    assert card_array[0] in RANKS
    assert card_array[1] in SUITE
    return card


class Player(object):
    def __init__(self, id, card_1, card_2, card_3):
        self.id = id
        self.card_1 = assert_suite(card_1)
        self.card_2 = assert_suite(card_2)
        self.card_3 = assert_suite(str(card_3).strip())

    # omitting getters/setters

    def get_hand(self):
        return [self.card_1, self.card_2, self.card_3]

    def get_rank(self, card): return card[0]

    def get_suite(self, card): return card[1]

    def is_flush(self):
        return True \
            if list(self.get_suite(self.card_1)) == list(self.get_suite(self.card_2)) \
               and list(self.get_suite(self.card_1)) == list(self.get_suite(self.card_3)) \
               and list(self.get_suite(self.card_1)) == list(self.get_suite(self.card_3)) \
            else False

    def is_kind(self):
        ranks = self.card_ranks()
        return True if sum(ranks) == ranks[0] * len(ranks) else False

    def is_pair(self):
        return True \
            if self.get_rank(self.card_1) == self.get_rank(self.card_2) and \
               self.get_rank(self.card_1) != self.get_rank(self.card_3) \
               or self.get_rank(self.card_1) == self.get_suite(self.card_3) and \
                  self.get_rank(self.card_1) != self.get_rank(self.card_2) \
               or self.get_rank(self.card_2) == self.get_rank(self.card_3) and \
                  self.get_rank(self.card_2) != self.get_rank(self.card_1) \
                  and self.get_rank(self.card_3) != self.get_rank(self.card_1) \
            else False

    def is_straight(self):
        ranks = self.card_ranks()
        return True if sum(ranks) == ranks[0] * len(ranks) - len(ranks) else False

    def card_ranks(self):
        ranks = ['--23456789TJQKA'.index(r) for r, s in self.get_hand()]
        ranks.sort(reverse=True)
        return ranks

    def __str__(self):
        return 'Player => id: {}, card_1: {}, card_2: {}, card_3: {}' \
            .format(self.id, self.card_1, self.card_2, self.card_3)


class RankOfHands:
    STRAIGHT_FLUSH = 1
    FLUSH = 2
    STRAIGHT = 3
    KIND = 4
    PAIR = 5
    HIGH_CARD = 6

    @staticmethod
    def get_ranks():
        return [
            RankOfHands.STRAIGHT_FLUSH,
            RankOfHands.FLUSH,
            RankOfHands.STRAIGHT,
            RankOfHands.KIND,
            RankOfHands.PAIR,
            RankOfHands.HIGH_CARD
        ]


def setup(data=None):
    players = []
    registered_ids = []
    player_min_max_test = False
    game_cards = get_game_cards()

    for line in data:
        if not player_min_max_test:
            assert 0 < int(line) < 24
            player_min_max_test = True
            assert int(data[0]) == (len(data) - 1)
            continue

        init = line.split(' ')
        players.append(
                Player(assert_unique_id(int(init[0]), registered_ids),
                       game_cards.pop(game_cards.index(init[1])),
                       game_cards.pop(game_cards.index(init[2])),
                       game_cards.pop(game_cards.index(init[3]))))

    return players


def new_result_table():
    return {
        RankOfHands.STRAIGHT_FLUSH: [],
        RankOfHands.FLUSH: [],
        RankOfHands.STRAIGHT: [],
        RankOfHands.KIND: [],
        RankOfHands.PAIR: [],
        RankOfHands.HIGH_CARD: [],
    }


def play(players):
    result_table = new_result_table()

    for player in players:
        if player.is_straight() and player.is_flush():
            result_table[RankOfHands.STRAIGHT_FLUSH].append({'id': player.id, 'card_ranks': player.card_ranks()})
        elif player.is_flush():
            result_table[RankOfHands.FLUSH].append({'id': player.id, 'card_ranks': player.card_ranks()})
        elif player.is_straight():
            result_table[RankOfHands.STRAIGHT].append({'id': player.id, 'card_ranks': player.card_ranks()})
        elif player.is_kind():
            result_table[RankOfHands.KIND].append({'id': player.id, 'card_ranks': player.card_ranks()})
        elif player.is_pair():
            result_table[RankOfHands.PAIR].append({'id': player.id, 'card_ranks': player.card_ranks()})
        else:
            result_table[RankOfHands.HIGH_CARD].append({'id': player.id, 'card_ranks': player.card_ranks()})

    return result_table


def get_winner(hand):
    winner = ''; max = 0
    for p in hand:
        if p['card_ranks'][0] > max:
            max = p['card_ranks'][0]
            winner = '{} '.format(p['id'])
        elif p['card_ranks'][0] == max:
            winner += '{} '.format(p['id'])
    return winner.strip()


def get_pair_winner(hand):
    winner = ''; max = 0; other_max = 0
    for p in hand:
        if p['card_ranks'][0] == p['card_ranks'][1]: pair = p['card_ranks'][0]; other = p['card_ranks'][2]
        elif p['card_ranks'][0] == p['card_ranks'][2]: pair = p['card_ranks'][0]; other = p['card_ranks'][1]
        else: pair = p['card_ranks'][1]; other = p['card_ranks'][0]

        if pair > max:
                max = pair; other_max = other
                winner = '{} '.format(p['id'])
        elif pair == max:
            if other > other_max:
                other_max = other; winner = '{} '.format(p['id'])
            elif other == other_max:
                winner += '{} '.format(p['id'])

    return winner.strip()


def get_high_card_winner(hand):
    winner = ''; max_1 = max_2 = max_3 = 0
    for p in hand:
        card_1 = p['card_ranks'][0]
        card_2 = p['card_ranks'][1]
        card_3 = p['card_ranks'][2]

        if card_1 > max_1:
            max_1 = card_1; max_2 = card_2; max_3 = card_3
            winner = '{} '.format(p['id'])
        elif card_1 == max_1:
            if card_2 > max_2:
                max_2 = card_2
                winner = '{} '.format(p['id'])
            elif card_2 == max_2:
                if card_3 > max_3:
                    max_3 = card_3
                    winner = '{} '.format(p['id'])
                elif card_3 == max_3:
                    winner += '{} '.format(p['id'])

    return winner.strip()


def announce_winner(play_results):
    for rank in RankOfHands.get_ranks():
        if rank == RankOfHands.PAIR:
            winner = get_pair_winner(play_results[rank])
            if winner: return winner
        elif rank == RankOfHands.HIGH_CARD:
            winner = get_high_card_winner(play_results[rank])
            if winner: return winner
        winner = get_winner(play_results[rank])
        if winner: return winner