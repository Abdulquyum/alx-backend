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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        
        if start >= len(dataset):
            return []
            
        return dataset[start:end]

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """ returns a tuple with start and end pages """
        start = (page - 1) * page_size
        end = start + page_size

        return ((start, end))
 