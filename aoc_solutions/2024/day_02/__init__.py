import sys
from pathlib import Path

from aoc.base import BaseChallenge
from aoc.input_providers import SingleFileInputProvider, SmartFileInputProvider


class Challenge(BaseChallenge):

    @staticmethod
    def check_report(report: list[str]) -> int:
        """
        :return: 1 if safe, 0 if not
        """
        prev = int(report[0])
        raising = int(report[0]) < int(report[-1])
        for level_str in report[1:]:
            level = int(level_str)
            if (abs(level - prev) > 3
                or raising and level < prev
                or not raising and level > prev
                or level == prev
            ):
                return 0
            prev = level
        return 1

    @staticmethod
    def check_report_dampened(report: list[str], dampened: bool = False, orig: list[str] = []) -> int:
        """
        :return: 1 if safe, 0 if not
        """
        prev = int(report[0])
        raising = int(report[0]) < int(report[-1])
        for idx, level_str in enumerate(report[1:], start=1):
            level = int(level_str)
            if (abs(level - prev) > 3
                or raising and level < prev
                or not raising and level > prev
                or level == prev
            ):
                if not dampened:
                    if Challenge.check_report_dampened(report[:idx] + report[idx+1:], dampened=True, orig=report):
                        break
                    else:
                        return Challenge.check_report_dampened(report[:idx-1] + report[idx:], dampened=True, orig=report)
                print(f"Wrong report - already dampened: {report} [orig: {orig}]")
                return 0
            prev = level
        return 1

    def part_1(self, input_lines: list[str]) -> int | str:
        return sum(
            self.check_report(line.split(" "))
            for line in input_lines
        )

    def part_2(self, input_lines: list[str]) -> int | str:
        return sum(
            self.check_report_dampened(line.split(" "))
            for line in input_lines
        )


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
