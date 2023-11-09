import os


def file_open(file_path):
    print("Opening and closing the file.\n")
    f = open(file_path, "r")
    return f

def read_char(f):
    f.seek(0)
    print("Reading charactiers from the file.")
    print(f.read(1))
    print(f.read(5), "\n")


def read_entire(f):
    f.seek(0)
    print("Reading the entire file at once.")
    print(f.read(), "\n")


def read_line(f):
    f.seek(0)
    print("Reading one line at a time.")
    print(f.readline())
    print(f.readline())
    print(f.readline(), "\n")


def read_list(f):
    f.seek(0)
    print("Reading the entire file into a list.")
    lines = f.readlines()
    print(lines)
    print(len(lines))
    for i in lines:
        print(i)
    print("")

def read_loop(f):
    f.seek(0)
    print("Looping through the file, line by line.")
    for i in f:
        print(i)
    print("")

if __name__ == '__main__':
    path = os.getcwd()
    file_path = os.path.join(path, "read_it.txt")
    f = file_open(file_path)

    read_char(f)
    read_entire(f)
    read_char(f)
    read_line(f)
    read_list(f)
    read_loop(f)

    f.close()