#!/usr/bin/env python3

import re


def find_words_in_file(input_file, output_file, pattern):
    """
    Reads a file line by line, finds words matching a regex pattern,
    and writes line number + word to output file.
    """

    with open(input_file, 'r') as in_stream:
        with open(output_file, 'w') as out_stream:
            for line_number, line in enumerate(in_stream, start=1):
                matches = re.findall(pattern, line, re.IGNORECASE)

                for match in matches:
                    out_stream.write(f"{line_number}\t{match}\n")


def main():
    input_file = "origin.txt"
    output_file = "output.txt"

    # regex for inheritance-related words
    pattern = r"\binherit\w*\b"

    find_words_in_file(input_file, output_file, pattern)

    print("Done! Results written to output.txt")


if __name__ == "__main__":
    main()
