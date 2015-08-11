from emotient import EmotientAnalyticsAPI
import argparse
import sys


def batch_delete(params):
    client = EmotientAnalyticsAPI(params['apikey'])
    media_list = client.media.all(page=1)
    if not params['bypass']:
        check = raw_input("Are you sure you want to delete all your videos? This is irreversible. (y/n):")
        if check.lower() != "y":
            print("Exiting, doing nothing.")
            sys.exit(0)

    print("Deleting...")
    for media in media_list:
        media.delete()
    print("All done!")



def read_command_line():
    parser = argparse.ArgumentParser(prog='deleter',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Deletes all videos from a given account.')
    parser.add_argument('-k', '--key', nargs=1, metavar='APIKEY', required=True, help='Your API Key')
    parser.add_argument('-y', '--yes', action='store_true', required=False, help='Bypass confirmation step')
    return parser.parse_args()


def process_command_line(args):

    if args.key is not None:
        apikey = args.key[0]

    return {'apikey': apikey, 'bypass': args.yes}


def main():
    args = read_command_line()
    params = process_command_line(args)
    batch_delete(params)


if __name__ == '__main__':
    main()