#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def multiply_new(*args):
    if args:
        min_i = args.index(min(args)) + 1
        max_i = args.index(max(args))
        return math.prod(args[min_i:max_i])
    else:
        return None


if __name__ == "__main__":
    print(f'Произведение чисел между макс и мин: {multiply_new(3,6,7,9)}')
