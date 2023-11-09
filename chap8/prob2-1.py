import os

def file_open_to_write(file_path):
    f = open(file_path, "w")
    return f

def file_read(file_path):
    f = open(file_path, "r")
    print(f.read())
    f.close()

if __name__ == '__main__':
    path = os.getcwd()

    write_file_path = os.path.join(path, "write_it.txt")
    f_write = file_open_to_write(write_file_path)

    writelines_file_path = os.path.join(path, "writelines_it.txt")
    f_writelines = file_open_to_write(writelines_file_path)

    line1 = "Line 1\n"
    line2 = "This is line 2\n"
    line3 = "That make this line 3\n"

    print("Creating a text file with the write() method.\n")
    f_write.write(line1)
    f_write.write(line2)
    f_write.write(line3)
    f_write.close()

    print("Reading the newly created file.")
    file_read(write_file_path)

    print("Creating a text file with the writelines() method.\n")
    lines = [line1, line2, line3]
    f_writelines.writelines(lines)
    f_writelines.close()

    print("Reading the newly created file.")
    file_read(writelines_file_path)






