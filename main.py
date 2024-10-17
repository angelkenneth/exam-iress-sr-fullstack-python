#!/usr/bin/python3
import logging

from app.run.from_stdin import intake_commands_from_input

logging.basicConfig(level=logging.INFO)


def main():
    intake_commands_from_input()


if __name__ == '__main__':  # pragma: no cover
    main()
