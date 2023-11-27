from __future__ import annotations

from typing import List

import pytest

from palgo.algo import Complexity
from palgo.algo.sort import SortAlgorithm
from palgo.algo.sort import validate_sorted_list


class MyCorrectSortAlgorithm(SortAlgorithm):
    """Correct sort algorithm that returns the input numbers in ascending order."""

    def complexity(self) -> Complexity:
        return super().complexity

    def sort(self) -> List[int]:
        self.numbers = sorted(self.numbers)
        return self.numbers


class MyIncorrectSortAlgorithm(SortAlgorithm):
    """Incorrect sort algorithm that returns the input numbers in descending order."""

    def complexity(self) -> Complexity:
        return super().complexity

    def sort(self) -> List[int]:
        self.numbers = MyCorrectSortAlgorithm(*self.numbers).sort()
        self.numbers.reverse()
        return self.numbers


class TestSortAlgorithm:
    @pytest.fixture
    def numbers(self) -> List[int]:
        return [4, 2, 7, 9, 1, 2]

    def test_sort_algorithm_receives_integers(self) -> None:
        with pytest.raises(TypeError):
            MyCorrectSortAlgorithm(1, 2, 3, "not an integer")

    def test_valid_algorithm_construction(self, numbers: List[int]) -> None:
        assert MyCorrectSortAlgorithm(*numbers).numbers == [4, 2, 7, 9, 1, 2]

    def test_valid_sort(self, numbers: List[int]) -> None:
        assert validate_sorted_list(MyCorrectSortAlgorithm(*numbers).sort())
