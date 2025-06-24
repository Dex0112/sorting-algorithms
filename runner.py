import subprocess
import sys

tests_path = "./tests.txt"
expected_path = "./results.txt"

bold = "\033[1m"
green = "\033[92m"
red = "\033[91m"
reset = "\033[0m"


def display_tests(results, expected):
    for i, (result, expect) in enumerate(zip(results, expected)):
        passed = result == expect
        color = green if passed else red
        status = "Passed!" if passed else "Failed!"

        print(f"Test {i + 1}: {bold}{color}{status}{reset}")
        print(f"{color}{'Result:'.ljust(10, " ")} {result.rstrip()}{reset}")
        print(f"{color}{'Expected:'.ljust(10, " ")} {expect}{reset}")


if __name__ == "__main__":
    print("".ljust(len("*Running...*"), '*'))
    print(f"{bold}*Running...*{reset}")
    print("".ljust(len("*Running...*"), '*'))

    results = []

    with open(tests_path, 'r') as file:
        for test in file.readlines():
            proc = subprocess.run(["python3", sys.argv[1], test],
                                  capture_output=True, text=True)
            results.append(proc.stdout)

    # Change to only run 1 test at a time

    with open(expected_path, 'r') as file:
        display_tests(results, file.readlines())

    print("".ljust(len("*Finished...*"), '*'))
    print(f"{bold}*Finished...*{reset}")
    print("".ljust(len("*Finished...*"), '*'))
