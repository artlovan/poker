import unittest
import pocker


class PockerTests(unittest.TestCase):

    def test_one_straight_flush_highest_sf_user_0_wins(self):
        players = pocker.setup(['3',
                                '0 Qc Kc Ac',
                                '1 Kd 5h 6c',
                                '2 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_two_straight_flush_highest_sf_user_0_1_wins(self):
        players = pocker.setup(['3',
                                '0 Qc Kc Ac',
                                '1 Qh Kh Ah',
                                '2 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1'

    def test_two_straight_flush_highest_sf_user_0_1_wins_cards_in_different_order(self):
        players = pocker.setup(['3',
                                '0 Qc Kc Ac',
                                '1 Ah Kh Qh',
                                '2 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1'

    def test_two_straight_flush_highest_sf_user_0_1_2_wins(self):
        players = pocker.setup(['3',
                                '0 Qc Kc Ac',
                                '1 Qh Kh Ah',
                                '2 Qs Ks As'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1 2'

    def test_pair_beats_high_cards(self):
        players = pocker.setup(['3',
                                '0 2c As 4d',
                                '1 Kd 5h 6c',
                                '2 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '2'

    def test_high_card_winner(self):
        players = pocker.setup(['3',
                                '0 Kh 4d 3c',
                                '1 Jd 5c 7s',
                                '2 9s 3h 2d'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_two_player_with_same_card_raises_ValueError(self):
        with self.assertRaises(ValueError):
            pocker.setup(['3',
                          '0 Kh 4d 3c',
                          '1 Kh 5c 7s',
                          '2 9s 3h 2d'])

    def test_player_has_not_existing_card_raises_ValueError(self):
        with self.assertRaises(ValueError):
            pocker.setup(['3',
                          '0 2x 4d 3c',
                          '1 Kh 5c 7s',
                          '2 9s 3h 2d'])

    def test_one_player_is_the_winner(self):
        players = pocker.setup(['1',
                                '0 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_one_player_is_the_winner_with_id_2(self):
        players = pocker.setup(['1',
                                '2 Jc Jd 9s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '2'

    def test_no_player_n_is_0(self):
        with self.assertRaises(AssertionError):
            pocker.setup(['0',
                          '2 Jc Jd 9s'])

        with self.assertRaises(AssertionError):
            pocker.setup(['0'])

    def test_too_many_player_n_is_grater_23(self):
        with self.assertRaises(AssertionError):
            pocker.setup(['24',
                          '2 Jc Jd 9s'])

        with self.assertRaises(AssertionError):
            pocker.setup(['24'])

    def test_n_is_not_a_number(self):
        with self.assertRaises(ValueError):
            pocker.setup(['a', '2 Jc Jd 9s'])

    def test_many_player_one_wins(self):
        players = pocker.setup(['11',
                                '0 Kh 4d 3d',
                                '1 Td 4c 2s',
                                '2 Jh 3c 3s',
                                '3 Js 2c 4s',
                                '4 Jc 5c 5s',
                                '5 Qh 5h 7c',
                                '6 6s 6c 7s',
                                '7 Qs Qd 8s',
                                '8 Th Ks 8h',
                                '9 Qc 6d 9h',
                                '10 9s 3h Jd'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '7'

    def test_two_pairs_one_wins(self):
        players = pocker.setup(['2',
                                '0 Qs Qd 8s',
                                '1 Qh Qc 7h'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_two_pairs_both_win(self):
        players = pocker.setup(['2',
                                '0 Qs Qd 8s',
                                '1 Qh Qc 8h'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1'

    def test_two_pairs_both_win_player_id_not_in_increment(self):
        players = pocker.setup(['2',
                                '7 Qs Qd 8s',
                                '8 Qh Qc 8h'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '7 8'

    def test_flush_beats_straight(self):
        players = pocker.setup(['2',
                                '1 2s 3s 5s',
                                '2 3h 4c 5h'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '1'

    def test_high_card_one_wins(self):
        players = pocker.setup(['3',
                                '0 8s 3d 5c',
                                '1 3h 4c 7s',
                                '2 7h 4s 3s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_high_card_first_high_equal_one_wins(self):
        players = pocker.setup(['3',
                                '0 8s 3d 5c',
                                '1 3h 4c 8c',
                                '2 7h 4s 3s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0'

    def test_high_card_two_high_equal_one_wins(self):
        players = pocker.setup(['3',
                                '0 8s 4d 2c',
                                '1 3h 4c 8c',
                                '2 7h 4s 3s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '1'

    def test_high_card_tree_high_equal_two_win(self):
        players = pocker.setup(['3',
                                '0 8s 4d 2c',
                                '1 2h 4c 8c',
                                '2 7h 4s 3s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1'

    def test_high_card_tree_high_equal_tree_win(self):
        players = pocker.setup(['3',
                                '0 8s 4d 2c',
                                '1 2h 4c 8c',
                                '2 8d 4s 2s'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '0 1 2'

    def test_three_of_a_kind_one_winner(self):
        players = pocker.setup(['3',
                                '0 4c 4h 4d',
                                '1 2c 2h 2d',
                                '2 5c 5h 5d'])
        winner = pocker.announce_winner(pocker.play(players))
        assert winner == '2'

    def test_two_players_with_same_id(self):
        with self.assertRaises(ValueError):
            pocker.setup(['2',
                          '0 4c 4h 4d',
                          '0 2c 2h 2d'])

    def test_n_is_less_then_number_of_players(self):
        with self.assertRaises(AssertionError):
            pocker.setup(['1',
                          '0 4c 4h 4d',
                          '0 2c 2h 2d'])

    def test_n_is_grater_then_number_of_players(self):
        with self.assertRaises(AssertionError):
            pocker.setup(['3',
                          '0 4c 4h 4d',
                          '0 2c 2h 2d'])


if __name__ == '__main__':
    unittest.main()
