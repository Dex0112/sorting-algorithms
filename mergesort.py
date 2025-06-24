import sys
import input_parser


def merge(arr1, arr2):
    merged = []

    l, r = 0, 0

    while l < len(arr1) or r < len(arr2):
        if l >= len(arr1):
            merged.append(arr2[r])
            r += 1
            continue

        if r >= len(arr2):
            merged.append(arr1[l])
            l += 1
            continue

        if arr1[l] < arr2[r]:
            merged.append(arr1[l])
            l += 1
            continue

        merged.append(arr2[r])
        r += 1
        continue

    return merged


def mergesort(lo, hi, arr):
    if lo == hi:
        # There is only a signle element
        return [arr[lo]]

    mid = (lo + hi) // 2

    # Sort left
    left = mergesort(lo, mid, arr)
    # Sort right
    right = mergesort(mid + 1, hi, arr)

    # Merge lerf + right
    return merge(left, right)


if __name__ == "__main__":
    arr = input_parser.parse_input_arr(sys.argv[1])

    sorted = mergesort(0, len(arr) - 1, arr)

    print(" ".join(map(str, sorted)))
