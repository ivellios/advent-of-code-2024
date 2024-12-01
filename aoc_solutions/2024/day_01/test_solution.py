from aoc.base_tests import BaseTestChallenge, Empty

from . import Challenge


class TestChallenge(BaseTestChallenge):
    challenge_class = Challenge
    expected_results_from_test_data = (11, 31)
    expected_results_from_real_data = (936063, Empty)
