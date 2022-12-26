#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def geometric_mean(*args):
    if args:
        nums = [num for num in args]
        out = math.pow(math.prod(nums), 1 / len(nums))
        return out
    else:
        return None


if __name__ == "__main__":
    print(f'Среднее геометрическое: {geometric_mean(2, 5, 6, 8)}')
