import pytest

# we want to have pytest assert introspection in the helpers
pytest.register_assert_rewrite('aoc.base_tests')
