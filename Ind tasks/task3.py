#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_substring(text, sub):
    if len(text) < len(sub):
        return 0

    if text.startswith(sub):
        return 1 + count_substring(text[len(sub):], sub)
    else:
        return count_substring(text[1:], sub)


if __name__ == "__main__":
    print(count_substring("banana", "ana"))
    print(count_substring("aaaa", "aa"))
    print(count_substring("ананас", "ана"))