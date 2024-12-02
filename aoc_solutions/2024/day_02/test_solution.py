
from aoc.base_tests import BaseTestChallenge, Empty

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (2, 4)
    expected_results_from_real_data = (472, 520)

    def test_simple_1(self):
        assert Challenge.check_report(['8', '10', '12', '13', '15']) == 1