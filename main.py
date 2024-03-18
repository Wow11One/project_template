from app.io.input import *
from app.io.output import *


def main():
    print(read_text_from_console())  # just print whatever user wrote in a console
    print("read file by pandas result:")
    print(read_text_from_file_by_pandas("text/pandas.txt"))  # prints a table from text file
    text_from_hello_file = read_text_from_file_by_python_tools("text/hello.txt")  # read text from file
    print("read file by python result:")
    print(text_from_hello_file)
    new_file = "text/new.txt"
    write_text_to_file(text_from_hello_file, new_file)  # write the text that was read before to a new file
    text_from_new_file = read_text_from_file_by_python_tools(new_file)
    print(text_from_new_file == text_from_hello_file)  # assert that text we've written is the same that we've read


if __name__ == '__main__':
    main()
