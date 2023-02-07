import logging
import random
import sys
from copy import copy
from typing import List

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def _swap(numbers: List[int], idx: int):
    if numbers[idx - 1] > numbers[idx]:
        numbers[idx - 1], numbers[idx] = numbers[idx], numbers[idx - 1]
    if idx - 2 >= 0:
        _swap(numbers, idx - 1)
    else:
        logger.debug({"action": "_swap", "numbers": numbers})


def insersion_sort_recursion(numbers: List[int], len_numbers: int, idx: int):
    _swap(numbers, idx)
    if idx + 1 < len_numbers:
        insersion_sort_recursion(numbers, len_numbers, idx + 1)
    else:
        logger.info({"action": "_insersion_sort_recursion", "numbers": numbers})


def insersion_sort(numbers: List[int]):
    len_numbers = len(numbers)
    for base_idx in range(1, len_numbers):
        for idx in range(base_idx, 0, -1):
            if numbers[idx - 1] > numbers[idx]:
                numbers[idx - 1], numbers[idx] = numbers[idx], numbers[idx - 1]
    logger.info({"action": "_insersion_sort", "numbers": numbers})


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for _ in range(10)]
    len_numbers = len(numbers)
    logger.info({"numbers": numbers})
    _numbers = copy(numbers)
    insersion_sort_recursion(_numbers, len_numbers, 1)
    _numbers = copy(numbers)
    insersion_sort(_numbers)
