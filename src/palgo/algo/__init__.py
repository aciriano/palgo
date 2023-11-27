from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from enum import Enum


class Complexity(Enum):
    """
    Enum to represent time complexity notations.

    Each member represents a common time complexity and includes a string
    representation of the Big O notation.
    """

    NOT_DEFINED = "Unknown"
    CONSTANT = "O(1)"
    LOGARITHMIC = "O(log n)"
    LINEAR = "O(n)"
    LINEAR_LOGARITHMIC = "O(n log n)"
    QUADRATIC = "O(n^2)"
    CUBIC = "O(n^3)"
    EXPONENTIAL = "O(2^n)"
    FACTORIAL = "O(n!)"


class Algorithm(ABC):
    @property
    @abstractmethod
    def complexity(self) -> Complexity:
        """
        Abstract property to represent the time complexity of the algorithm.

        This property must be implemented by each subclass to provide
        information about the time complexity of the specific algorithm.

        :return: The time complexity of the algorithm.
        :rtype: Complexity
        """
        return Complexity.NOT_DEFINED
