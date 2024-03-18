import unittest

from pandas import DataFrame

from app.io.input import *
from app.io.output import *


class TestInput(unittest.TestCase):
    # tests for the second function of an input.py file "read_text_from_file"
    # that returns text from a file by built in python tools
    def test_read_text_from_file_empty(self):
        empty_filename = "text/empty.txt"
        write_text_to_file("", empty_filename)
        self.assertEqual(len(read_text_from_file(empty_filename)), 0)  # empty.txt is always empty

    def test_read_text_from_file_successful(self):
        initial_text = "test"
        new_filename = "text/new.txt"
        write_text_to_file(initial_text, new_filename)  # create a new file and insert text
        text = read_text_from_file(new_filename)  # read inserted text
        self.assertEqual(initial_text, text)

    def test_read_text_from_file_fails(self):
        nonexistent_filename = "text/nonexistent.txt"
        # assert that if file does not exist method raises an error
        self.assertRaises(FileNotFoundError, read_text_from_file, nonexistent_filename)

    # tests for the third function of an input.py file "read_text_from_file_by_pandas"
    # that returns table-like text from a file by pandas library

    def test_read_text_from_file_by_pandas_successful(self):
        initial_text = """John  25  170
                          Alice 28  165
                          Bob   30  180"""
        pandas_filename = "text/pandas.txt"
        write_text_to_file(initial_text, pandas_filename)  # create a new file and insert text
        table = read_text_from_file_by_pandas(pandas_filename)  # read inserted text
        # because this function returns a new table,
        # so strings are not equal
        self.assertNotEqual(initial_text, DataFrame.to_string(table))
        # we check if our method added headers that we needed
        self.assertIn("Name", DataFrame.to_string(table))
        self.assertIn("Age", DataFrame.to_string(table))
        self.assertIn("Height", DataFrame.to_string(table))

    def test_read_text_from_file_by_pandas_empty_successful(self):
        empty_text = ""
        empty_filename = "text/empty.txt"
        write_text_to_file(empty_text, empty_filename)
        empty_table = read_text_from_file_by_pandas(empty_filename)
        self.assertTrue(empty_table.empty)

    def test_read_text_from_file_by_pandas_fails(self):
        nonexistent_filename = "text/nonexistent.txt"
        # assert that if file does not exist method raises an error
        self.assertRaises(FileNotFoundError, read_text_from_file_by_pandas, nonexistent_filename)
