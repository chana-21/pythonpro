import pickle
import shelve
import os


def file_write_pickle(file_path):
    f = open(file_path, "wb")
    variety = ["sweet", "hot", "dill"]
    shape = ["whole", "spear", "chip"]
    brand = ["Claussen", "Heinz", "Vlassic"]

    pickle.dump(variety, f)
    pickle.dump(shape, f)
    pickle.dump(brand, f)

    f.close()

def file_read_pickle(file_path):
    f = open(file_path, "rb")

    variety = pickle.load(f)
    shape = pickle.load(f)
    brand = pickle.load(f)

    print(variety)
    print(shape)
    print(brand)

    f.close()

def file_write_shelve(file_path):
    f = shelve.open(file_path)

    f["variety"] = ["sweet", "hot", "dill"]
    f["shape"] = ["whole", "spear", "chip"]
    f["brand"] = ["Claussen", "Heinz", "Vlassic"]

    f.sync()
    f.close()


def file_read_shelve(file_path):
    f = shelve.open(file_path)

    for key in f.keys():
        print(key, "-", f[key])

    f.close()

if __name__ == '__main__':
    path = os.getcwd()

    shelve_file_path = os.path.join(path, "shelve.db")
    pickle_file_path = os.path.join(path, "pickle.db")

    file_write_shelve(shelve_file_path)
    file_read_shelve(shelve_file_path)

    file_write_pickle(pickle_file_path)
    file_read_pickle(pickle_file_path)