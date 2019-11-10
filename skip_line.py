# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program loops from 1000 to 2000


def main():

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("")
            print(counter, "", end="")
        else:
            print(counter, "", end="")


if __name__ == "__main__":
    main()
