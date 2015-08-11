from emotient import EmotientAnalyticsAPI
import argparse
import os

# This script assumes that your video files are properly named with three letter extensions.
def batch_upload(api_key, directory):
    client = EmotientAnalyticsAPI(api_key)
    valid_ext = ['.avi', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.wmv']
    print("Uploading...")
    for subdir, dirs, files in os.walk(directory):
        for f in files:
            filename, extension = os.path.splitext(f)
            if extension in valid_ext:
                filepath = os.path.join(subdir, f)
                with open(filepath, 'rb') as fp:
                    client.media.upload(fp)
    print("All done!")


def read_command_line():
    parser = argparse.ArgumentParser(prog='deleter',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Uploads all videos with valid file extensions from a given directory.')
    parser.add_argument('-k', '--key', nargs=1, metavar='APIKEY', required=True, help='Your API Key')
    parser.add_argument('-d', '--directory', nargs=1, metavar='DIR', required=True, help='Folder path to upload from')
    return parser.parse_args()


def process_command_line(args):

    if args.key is not None:
        apikey = args.key[0]
    if args.directory is not None:
        upload_dir = args.directory[0]

    return {'upload_dir': upload_dir, 'apikey': apikey}


def main():
    args = read_command_line()
    params = process_command_line(args)
    batch_upload(params['apikey'], params['upload_dir'])


if __name__ == '__main__':
    main()
