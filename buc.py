import sys
import getopt
import argparse
import configparser

from module.clean_user import clean_user

CONFIG_FILE = 'buc.ini'


# Get config.
def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


# Show help.
def help():
    parser = argparse.ArgumentParser(
        description='Clean inactive users in Bonita BPM')
    parser.add_argument('-a', '--all', action='store_true',
                        help='clean users include active users')
    args = parser.parse_args()


def main():
    # Get config.
    config = read_config()

    # Parse args.
    options = "ha"
    long_options = ["help", "all"]
    try:
        opts, args = getopt.getopt(sys.argv[1:], options, long_options)
    except getopt.GetoptError as err:
        print str(err)
        help()
        sys.exit()

    all = False
    for o, a in opts:
        # Show help.
        if o in ("-h", "--help"):
            help()
            sys.exit()
        # Clean user include active users.
        elif o in ("-a", "--all"):
            all = True
        else:
            assert False, "unhandled option"
    # Clean inactive users.
    clean_user(config, all)


if __name__ == "__main__":
    main()
