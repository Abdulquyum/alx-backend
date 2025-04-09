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

# page_size: the length of the returned dataset page
# page: the current page number
# data: the dataset page (equivalent to return from previous task)
# next_page: number of the next page, None if no next page
# prev_page: number of the previous page, None if no previous page
# total_pages: the total number of pages in the dataset as an integer
# Make sure to reuse get_page in your implementation.

# You can use the math module if necessary.

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        data = dataset[start:end]
        next_page = page + 1
        prev_page = page - 1
        total_page = len(dataset)

        if start >= total_page:
            return []
            
        return ({
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_page
        })

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """ returns a tuple with start and end pages """
        start = (page - 1) * page_size
        end = start + page_size

        return ((start, end))
 