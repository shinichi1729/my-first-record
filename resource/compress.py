from typing import List
import bisect
"""
compression and rewriting of values.
time complexity is O(NlogN)
"""


def compress(values: List[int]) -> List[int]:
    vals = sorted(list(set(values)))
    for i in range(len(values)):
        values[i] = bisect.bisect_left(vals, values[i])
    return values
