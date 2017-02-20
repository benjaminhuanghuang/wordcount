import sys
import argparse
import wordcount_lib


def main():
    p = argparse.ArgumentParser()
    p.add_argument('filenames', nargs='+')  # nargs='+' means one or more 'filenames'
    args = p.parse_args()

    total_words = 0
    total_lines = 0
    total_chars = 0

    for filename in args.filenames:
        try:
            chars, words, lines = wordcount_lib.consume(filename)
        except IOError:
            print('error - %s does not exist!' % filename, file=sys.stderr)
            continue

        # track total
        total_words += words
        total_lines += lines
        total_chars += chars

    print('%d\t%d\t%d\tin %d files' % (total_chars, total_words, total_lines,
                                       len(args.filenames)))


if __name__ == '__main__':
    main()
