#!/usr/bin/python3
#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <ccurtis@mtroyal> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Charlotte Curtis
# ----------------------------------------------------------------------------
#
# A truly terrible program. Do not use for real data processing needs.

import sys
import random

def print_stuff(csv: str) -> None:
    """
    Prints stuff from the csv
    """
    with open(csv, "r") as f:
        header = f.readline().strip().split(",")
        for line in f:
            parts = line.strip().split(",")
            # make sure there's at least two columns
            if len(parts) > 1:
                x, y = [int(tok) for tok in parts]
                print(f"{x}/{y} = {x / y:0.2f}")


def make_data() -> None:
    """
    Generates some random data and saves it to input.csv.
    User gets no choice over length, distribution, filename, or anything really.
    """
    n = 20
    with open("input.csv", "w") as f:
        for _ in range(1000):
            f.write(f"{random.randint(0, n)},{random.randint(0, n)}\n")

    print("Data saved to input.csv")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} csv")
        response = input("Would you like to generate some random data instead? (y/n): ")

        if response.lower() == "y":
            make_data()
        
        exit(0)

    print_stuff(sys.argv[1])
