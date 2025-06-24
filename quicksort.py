import sys
import input_parser

if __name__ == "__main__":
    arr = input_parser.parse_input_arr(sys.argv[1])

    input_parser.print_arr(arr)
