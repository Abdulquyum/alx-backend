#!/usr/bin/env python3
""" an helper function for pagination """


def index_range(page: int, page_size: int) -> tuple:
    """ returns a tuple with start and end pages """
    start = (page - 1) * page_size
    end = start + page_size

    return ((start, end))
