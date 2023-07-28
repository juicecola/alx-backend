#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset.

        Returns:
            List[List]: The dataset excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create and return a dictionary of the dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: A dictionary containing the dataset indexed by sorting position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Get data for a given data range.

        Args:
            index (int): The starting index of the data range. Default is 0.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            Dict: A dictionary containing the data and metadata.
                Keys:
                    'index': The starting index of the data range.
                    'data': The dataset for the specified data range.
                    'page_size': The number of items per page.
                    'next_index': The next index to continue pagination.
        """
        # Validate the index and page_size
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []  # Collect all indexed data
        next_index = index

        while len(data) < page_size and next_index < len(self.indexed_dataset()):
            if self.indexed_dataset().get(next_index):
                data.append(self.indexed_dataset()[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }

