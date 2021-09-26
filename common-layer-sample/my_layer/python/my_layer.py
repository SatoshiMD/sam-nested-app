from typing import List


def sample_function() -> str:
    return 'sample_function'


def sample_summation(arr: List) -> int:
    result = 0
    for a in arr:
        result += a
    return result
