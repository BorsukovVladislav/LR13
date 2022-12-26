#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def average_harm(*args):
    if args:
        nums = [1/num for num in args]
        out = len(nums)/math.fsum(nums)
        return out
    else:
        return None


if __name__ == "__main__":
    print(f'Среднее гармоническое: {average_harm(5, 2, 3)}')
