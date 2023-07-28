#!/usr/bin/env python3

import csv
from typing import List, Dict, Union

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Get the dataset from the CSV file and cache it.

        Returns:
            List[List]: The dataset excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the dataset for a given data range.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: The dataset for the specified page and page size.
        """
        try:
            assert page > 0 and page_size > 0
            assert isinstance(page, int) and isinstance(page_size, int)
            start_index, end_index = index_range(page, page_size)
            dataset = self.dataset()[start_index:end_index]
            return dataset
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """
        Get metadata for a given data range.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary containing metadata.
            Keys:
                'page': The current page number.
                'page_size': The number of items per page.
                'data': The dataset for the specified page and page size.
                'next_page': The next page number. None if it's the last page.
                'prev_page': The previous page number. None if it's the first page.
                'total_pages': The total number of pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = None if (page + 1) > total_pages else page + 1
        prev_page = None if page - 1 < 1 else page - 1

        my_dict = {
            'page': page,
            'page_size': page_size,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return my_dict

