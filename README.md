"Poker"
=======

Sample usage:
-------------
players = pocker.setup(['3',
                        '0 Qc Kc Ac',
                        '1 Kd 5h 6c',
                        '2 Jc Jd 9s'])
winner = pocker.announce_winner(pocker.play(players))
assert winner == '0'


Run tests
---------

1. cd into pocker dir
2. issue command: python pocker_test.py


Notes:
------

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

