from __future__ import annotations

from abc import abstractmethod
from typing import List

from palgo.algo import Algorithm


class SortAlgorithm(Algorithm):
    """Base class for all sorting algorithms.

    Subclasses (e.g. BubbleSort) must implement the method `sort`, which returns the
    sequence of numbers in ascending order.
    """

    def __init__(self, *numbers: int) -> None:
        """
        Initialize the SortAlgorithm instance.

        :param *numbers: Variable number of integers to be sorted.
        :raises TypeError: If any element in *numbers is not an integer.
        """
        if not all(isinstance(i, int) for i in numbers):
            raise TypeError("All numbers must be integer numbers.")

        self.numbers = list(numbers)

    @abstractmethod
    def sort(self) -> List[int]:
        """Sort the sequence of numbers in ascending order.

        :return: The sorted sequence of numbers.
        :rtype: List[int]
        """
        ...


def validate_sorted_list(sorted_list: List[int]) -> bool:
    """Validate if a list is sorted in ascending order.

    :param sorted_list: The list to be validated.
    :type sorted_list: List[int]
    :return: True if the list is sorted, False otherwise.
    :rtype: bool
    """
    return sorted_list == sorted(sorted_list)
