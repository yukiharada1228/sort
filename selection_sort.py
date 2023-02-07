import logging
import random
import sys
from copy import copy
from typing import List

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def _min_idx(numbers: List[int], len_numbers: int, idx: int, min_idx: int):
    if numbers[idx] < numbers[min_idx]:
        min_idx = idx
    logger.debug({"action": "_min_idx", "min_idx": min_idx})
    return (
        _min_idx(numbers, len_numbers, idx + 1, min_idx)
        if idx + 1 < len_numbers
        else min_idx
    )


def _swap(numbers: List[int], len_numbers: int, idx: int):
    min_idx = _min_idx(numbers, len_numbers, idx + 1, idx)
    numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]
    logger.debug({"action": "_swap", "numbers": numbers})


def selection_sort_recursion(numbers: List[int], len_numbers: int, idx: int):
    _swap(numbers, len_numbers, idx)
    if len_numbers - 1 > idx + 1:
        selection_sort_recursion(numbers, len_numbers, idx + 1)
    else:
        logger.info({"action": "selection_sort_recursion", "numbers": numbers})


def selection_sort(numbers: List[int]):
    len_numbers = len(numbers)
    min_idx = 0
    for base_idx in range(len_numbers):
        min_idx = base_idx
        for idx in range(base_idx + 1, len_numbers):
            if numbers[idx] < numbers[min_idx]:
                min_idx = idx
        numbers[base_idx], numbers[min_idx] = numbers[min_idx], numbers[base_idx]
    logger.info({"action": "selection_sort", "numbers": numbers})


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for _ in range(10)]
    len_numbers = len(numbers)
    logger.info({"numbers": numbers})
    _numbers = copy(numbers)
    selection_sort_recursion(_numbers, len_numbers, 0)
    _numbers = copy(numbers)
    selection_sort(_numbers)
