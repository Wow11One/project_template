import pandas as pd


def read_text_from_console():
    """
    Reads data from console.

    Examples:
    >>> read_text_from_console()
    Enter your value: 21
    21
    >>> read_text_from_console()
    Enter your value: 12
    12
    Returns:
        str: The user's input value.
    """
    input_value = input("Enter your value: ")
    return input_value


def read_text_from_file_by_python_tools(filename):
    """
    Read data from file by built-in Python tools.
    Examples:
    >>> read_text_from_file_by_python_tools("text/hello.txt")
    "hello, python!"
    >>> read_text_from_file_by_python_tools("text/empty.txt")
    ""
    Args:
        filename (str): The name of file to read from.
    Returns:
        str: The content of the file.
    Raises:
        FileNotFoundError: if programm is unable to locate the file.
    """
    try:
        with open(filename, "r") as my_file:
            return my_file.read()
    except FileNotFoundError as e:
        print(e)
    finally:
        my_file.close()


def read_text_from_file_by_pandas(filename):
    """
    Read data from file as a table by tools of the pandas library.
    Examples:
    >>> read_text_from_file_by_pandas("text/pandas.txt")
            "Name  Age  Height
        0   John   25     170
        1  Alice   28     165
        2    Bob   30     180"
    >>> read_text_from_file_by_pandas("text/empty.txt")
    ""
    Args:
        filename (str): The name of file to read from.
    Returns:
        str: The content of the file as a table.
    Raises:
        FileNotFoundError: if programm is unable to locate the file.
    """
    df = pd.read_table(filename, sep="\s+", names=['Name', 'Age', 'Height'])
    return df
