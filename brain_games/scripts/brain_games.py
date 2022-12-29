#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    global user_name
    user_name = welcome_user()


if __name__ == '__main__':
    main()
