import re
import sys


def read_from_file():
    """Reads data from file, and strips everything that isn't written before 'item value'
    saves the values written after item value to an array called raw_data"""
    raw_data = []
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            if len(line) > 0:
                raw_data += re.findall(r"Item value: (.*)", line)
    return raw_data


def write_to_file(pw):
    # Writes data to new file. Appends prefix "CLEANED - " to filename.
    with open("Extracted passwords from - " + sys.argv[1], "w") as f:
        for x in pw:
            f.write(x + "\n")


passwords = read_from_file()
write_to_file(passwords)
