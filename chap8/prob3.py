import os


def file_write(file_path):
    f = open(file_path, "w")
    lines = []

    print("Input your string...")
    while True:
        enter = input('>> ')
        if enter == "Q" or enter == "q":
            break

        lines.append(enter + "\n")

    f.writelines(lines)
    f.close()
    print("Write process has been finished\n\n")


def file_read(file_path):
    f = open(file_path, "r")
    print("Your inputs are below...")
    print(f.read())


if __name__ == '__main__':
    path = os.getcwd()

    file_path = os.path.join(path, "write_and_read.txt")

    file_write(file_path)
    file_read(file_path)


