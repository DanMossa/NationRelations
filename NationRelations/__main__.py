import argparse

def main():
    """ Program entry point that will pass CLI args to nationrelations """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '-debug', dest='debug', action='store_true', help='Enable debug logging', )
    args = parser.parse_args()
    debug = args.debug
    
if __name__ == '__main__':
    print('in main')
    main()