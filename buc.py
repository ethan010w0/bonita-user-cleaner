import argparse
import configparser
import sys

from module.clean_user import clean_user

CONFIG_FILE = 'buc.ini'


# Get config.
def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def main():
    # Get config.
    config = read_config()

    # Parse args.
    parser = argparse.ArgumentParser(
        description='Clean inactive users in Bonita BPM')
    parser.add_argument('-a', '--all',
                        action='store_true',
                        help='clean users include active users')
    args = parser.parse_args()

    # Clean inactive users.
    clean_user(config, args.all)


if __name__ == "__main__":
    main()
