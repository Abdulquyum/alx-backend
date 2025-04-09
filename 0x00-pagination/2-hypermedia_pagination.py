#!/usr/bin/env python3
""" Hypermedia pagination """


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get a page of data from the dataset with hypermedia pagination.
        
        Args:
            page (int): The current page number
            page_size (int): The number of items per page
            
        Returns:
            dict: A dictionary containing:
                - page_size: the length of the returned dataset page
                - page: the current page number
                - data: the dataset page
                - next_page: number of the next page, None if no next page
                - prev_page: number of the previous page, None if no previous page
                - total_pages: the total number of pages in the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)
        
        # Get the data for the current page
        start, end = self.index_range(page, page_size)
        data = dataset[start:end]
        
        # Calculate next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """ returns a tuple with start and end pages """
        start = (page - 1) * page_size
        end = start + page_size

        return ((start, end))
 