import unittest

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
        text = read_text_from_file("text/new.txt")  # read inserted text
        self.assertEqual(initial_text, text)

    def test_read_text_from_file_fails(self):
        nonexistent_filename = "text/nonexistent.txt"
        # assert that if file does not exist method raises an error
        self.assertRaises(FileNotFoundError, read_text_from_file, nonexistent_filename)
