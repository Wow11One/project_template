def write_text_to_console(text):
    """
    write text from a parameter to console.
    Examples:
    >>> write_text_to_console("hello, python!")
    "hello, python!"
    >>> write_text_to_console("victory!")
    "victory"
    >>> write_text_to_console("")
    ""
    Args:
        text (str): The data to write to the console.
    Returns:
        None.
    """
    pass


def write_text_to_file(text, filename):
    """
    write text from a parameter to a file, which name
    is specified in filename parameter.
    If the file does not exist, it will be created.
    Examples:
    >>> expected_text = "hello, python!"
    >>> new_filename = "text/new.txt"
    >>> write_text_to_file(expected_text, new_filename)
    >>> actual_text = read_text_from_file_by_python_tools(new_filename)
    >>> assert actual_text == expected_text
    Args:
        text (str): The text to write to the console.
        filename (str): The name of the file to write the text.
    Returns:
        None.
    """
    pass
