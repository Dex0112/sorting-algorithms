import random


def generate_test(min, max, length):
    test = []
    for _ in range(0, length):
        rand_int = random.randint(min, max)
        test.append(rand_int)

    sorted_test = test[:]
    sorted_test.sort()

    return (test, sorted_test)


def write_tests(test_file, results_file, tests):
    with open(test_file, 'w') as file:
        for test in tests:
            file.write(" ".join(map(str, test[0])) + "\n")

    with open(results_file, 'w') as file:
        for result in tests:
            file.write(" ".join(map(str, result[1])) + "\n")


if __name__ == "__main__":
    print("Running...")

    tests = []
    num_tests = int(input("How many tests would you like to generate: "))
    test_len = int(input("Test length: "))
    test_min = int(input("Test minimum: "))
    test_max = int(input("Test maximum: "))

    for _ in range(0, num_tests):
        tests.append(generate_test(test_min, test_max, test_len))

    write_tests("./tests.txt", "./results.txt", tests)
    print("Tests Generated!")
