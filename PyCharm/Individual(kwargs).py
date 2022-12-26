#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def filter_kwargs(**kwargs):
    filters = ["a", "e", "i", "o"]
    params = [kwargs.get(k) for k in filters if kwargs.get(k)]
    return params


if __name__ == "__main__":
    print(filter_kwargs(a=1, b=2, c=3, d=4, e=5))
