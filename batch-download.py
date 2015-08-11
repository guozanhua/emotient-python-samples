from emotient import EmotientAnalyticsAPI
import os
import argparse

def save_raw_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-raw.csv")
    with open(filepath, 'w') as fp:
        media.analytics(fp)


def save_aggregate_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-aggregate.csv")
    with open(filepath, 'w') as fp:
        media.aggregated_analytics(fp, interval='summary', report='standard', gender='combined')


def save_core_quarter_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-core-quarter.csv")
    with open(filepath, 'w') as fp:
        media.aggregated_analytics(fp, interval='quarter', report='standard', gender='combined')


def save_core_second_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-core-second.csv")
    with open(filepath, 'w') as fp:
        media.aggregated_analytics(fp, interval='second', report='standard', gender='combined')


def save_adv_quarter_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-adv-quarter.csv")
    with open(filepath, 'w') as fp:
        media.aggregated_analytics(fp, interval='quarter', report='advanced', gender='combined')


def save_adv_second_data(media, filename, directory):
    filepath = os.path.join(directory, filename + "-adv-second.csv")
    with open(filepath, 'w') as fp:
        media.aggregated_analytics(fp, interval='second', report='advanced', gender='combined')

def read_command_line():
    parser = argparse.ArgumentParser(prog='downloader',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Downloads all CSV data for a given account.')
    parser.add_argument('-k', '--key', nargs=1, metavar='APIKEY', required=True, help='Your API Key')
    parser.add_argument('-d', '--directory', nargs=1, metavar='DIR', required=True, help='Where to download files')
    return parser.parse_args()

def process_command_line(args):

    if args.directory is not None:
        download_dir = args.directory[0]
    if args.key is not None:
        apikey = args.key[0]

    return {'download_dir': download_dir, 'apikey': apikey}


#directory path needs to be the full directory path ("/Users/etc")
def save_all_data(api_key, directory):
    client = EmotientAnalyticsAPI(api_key)
    media_list = client.media.all(page=1)
    # Check that path exists and create if necessary
    if not os.path.exists(directory):
        os.makedirs(directory)
    print("Downloading...")
    for media in media_list:
        # media_object = client.media.retrieve(media.id)
        media_object = media
        filename = media_object.data['filename']
        save_raw_data(media_object, filename, directory)
        save_aggregate_data(media_object, filename, directory)
        save_core_quarter_data(media_object, filename, directory)
        save_core_second_data(media_object, filename, directory)
        save_adv_quarter_data(media_object, filename, directory)
        save_adv_second_data(media_object, filename, directory)
    print("All done!")


def main():
    args = read_command_line()
    params = process_command_line(args)
    save_all_data(params['apikey'], params['download_dir'])


if __name__ == '__main__':
    main()