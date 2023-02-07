import logging
import random
import sys
from copy import copy
from typing import List

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def _bubble_sort_recursion(numbers: List[int], idx: int, max_idx: int):
    if numbers[idx] > numbers[idx + 1]:
        numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
    logger.debug({"action": "_bubble_sort_recursion", "numbers": numbers})
    if max_idx > idx + 1:
        return _bubble_sort_recursion(numbers, idx + 1, max_idx)


def bubble_sort_recursion(numbers: List[int], max_idx: int):
    _bubble_sort_recursion(numbers, 0, max_idx)
    logger.debug({"action": "bubble_sort_recursion", "numbers": numbers})
    if max_idx - 1 >= 1:
        return bubble_sort_recursion(numbers, max_idx - 1)


def bubble_sort(numbers: List[int]):
    for max_idx in range(len(numbers) - 1, 0, -1):
        for idx in range(max_idx):
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
    logger.debug({"action": "bubble_sort", "numbers": numbers})


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for _ in range(10)]
    len_numbers = len(numbers)
    logger.info({"numbers": numbers})
    bubble_sort_recursion(copy(numbers), len_numbers - 1)

    logger.info({"numbers": numbers})
    bubble_sort(copy(numbers))
