def parse_input_arr(arr_str):
    arr = list(map(int, arr_str.split(" ")))

    return arr


def print_arr(arr):
    print(" ".join(map(str, arr)))
