import bisect
import sys
from collections import defaultdict
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider



class Challenge(BaseChallenge):

    def part_1(self, input_lines: list[str]) -> int | str:
        list_1 = []
        list_2 = []
        for line in input_lines:
            num1, num2 = line.split("   ")
            bisect.insort(list_1, int(num1))
            bisect.insort(list_2, int(num2))

        return sum([abs(x - y) for x, y in zip(list_1, list_2)])

    def part_2(self, input_lines: list[str]) -> int | str:
        occurances = defaultdict(int)
        numbers = []

        for line in input_lines:
            num1, num2 = line.split("   ")
            numbers.append(int(num1))
            occurances[int(num2)] += 1

        return sum(occurances[number] * number for number in numbers)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_provider = SingleFileInputProvider(
            Challenge.year, Challenge.day, input_path=Path(sys.argv[1])
        )
        Challenge(input_provider).run()
    else:
        Challenge(
            SmartFileInputProvider(Challenge.year, Challenge.day, use_test_data=True)
        ).run()
        Challenge(SmartFileInputProvider(Challenge.year, Challenge.day)).run()
