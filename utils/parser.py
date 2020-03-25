from utils.test import Test

def normalize_row(row):
    return row[11: 58]

def parse(file_path):
    file = open(file_path, "r")

    tests = []

    row = file.readlines()
    for i in range(2, (2 + 3*128) * 9, 1 + 3 * 128):
        key = normalize_row(row[i])
        start = i + 2
        for j in range(start, start + 3 * 127 + 1, 3):
            value = normalize_row(row[j])
            result = normalize_row(row[j + 1])
            test = Test(value, key, result)
            tests.append(test)

    file.close()

    return tests