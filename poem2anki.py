#! /usr/bin/env python
#
# poem2anki.py
#
# Convert a text file into Anki flash cards.
# The question will be a certain number of lines, (default 3)
# and the response is the following line or lines (default 1).
# The source is read from stdin and the CSV for importing into
# Anki is sent to stdout.
#
# e.g.
#    ./poem2anki.py < sonnet18.txt > sonnet18.csv
#

import argparse
import sys
from collections import deque


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--qlines", type=int, default=3, 
        help="No. of lines in question")
    parser.add_argument("-a", "--alines", type=int, default=1, 
        help="No. of lines in answer")

    args = parser.parse_args()
    qlines = args.qlines
    alines = args.alines

    # Take out blank lines
    poem = [rl.strip() for rl in sys.stdin.readlines() 
                  if len(rl.strip()) > 0]

    questions = deque([""] * qlines)
    answers = deque([""] * alines)

    def cardshift(next_line):
        """
        We move the card through the poem by adding the next line
        to the answer and dropping the first line of the question.
        """
        answers.append(next_line)
        questions.append(answers.popleft())
        questions.popleft()

    line_reader = iter(poem)

    # Fill up the first card
    # We need one question line plus however many answer lines
    try:
        for i in range(1 + alines):
            cardshift(next(line_reader))
    except StopIteration:
        print >>sys.stderr, "Insufficient lines for a single card"
        sys.exit()

    # Then print cards until we run out of input lines
    try:
        while True:
            print ("<br />".join(questions), "\t", "<br />".join(answers))
            cardshift(next(line_reader))
    except StopIteration:
        pass


if __name__ == '__main__':
    main()