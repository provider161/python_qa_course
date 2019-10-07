"""
Simple log parser
"""

from collections import Counter
from operator import itemgetter

import argparse
import json
import os
import re
import sys


def get_args():
    """Arguments parser."""
    # parse script arguments and return it
    args = argparse.ArgumentParser()

    args.add_argument('--log-dir', type=str, action='store', help='Path to directory with *.log files')
    args.add_argument('--log-file', type=str, action='store',  help='Path to log file')

    return args.parse_args()


def read_file(log_file, out_file):
    """

    Parameters
    ----------
    log_file : str
        Path to file with logs.
    out_file : str
        Path to file to write results.

    Returns
    -------
    Write results to file in json format

    """
    requests_count = 0
    get_count = 0
    post_count = 0
    put_count = 0
    delete_count = 0
    patch_count = 0
    requests_list = []
    ip_list = []

    # open file with logs and read content line by line
    try:
        with open(log_file, 'r') as log:
            for line in log:

                # count number of HTTP requests types
                requests_count += 1

                if re.search('GET', line):
                    http_method = 'GET'
                    get_count += 1
                elif re.search('POST', line):
                    http_method = 'POST'
                    post_count += 1
                elif re.search('PUT', line):
                    http_method = 'PUT'
                    put_count += 1
                elif re.search('DELETE', line):
                    http_method = 'DELETE'
                    delete_count += 1
                elif re.search('PATCH', line):
                    http_method = 'PATCH'
                    patch_count += 1

                # collect all requests from log
                request_ip = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                request_duration = re.search(r'(\d)*$', line)
                request_url = re.search(r'(/\D*) HTTP', line)
                request_status_code = re.search(r'" (\d{3}) ', line)

                if request_ip and request_duration and request_url and request_status_code:
                    requests_list.append([request_ip.group(0),
                                          request_duration.group(0),
                                          http_method,
                                          request_url.group(1),
                                          request_status_code.group(1)])
                    ip_list.append(request_ip.group(0))

    except FileNotFoundError as read_exc:
        sys.exit(f'Unable to open log file because of error - {read_exc}')
    except FileExistsError as read_exc:
        sys.exit(f'Unable to open log file because of error - {read_exc}')

    # count top 10 ips from which requests came
    top_10_requests = list(sorted(Counter(ip_list).items(), key=lambda x: x[1], reverse=True))[:9]

    # count top 10 ips by request duration
    top_10_duration = sorted(requests_list, key=itemgetter(1), reverse=True)[:9]

    # count top 10 requests with client error
    top_10_client_error = [x for x in requests_list if x[4].startswith('4')][:9]

    # count top 10 requests with server error
    top_10_server_error = [x for x in requests_list if x[4].startswith('5')][:9]

    result = {
        'requests':
            {'all': requests_count,
             'get_count': get_count,
             'post_count': post_count,
             'put_count': put_count,
             'delete_count': delete_count,
             'patch_count': patch_count,
             },
        'top_10_requests': top_10_requests,
        'top_10_duration': top_10_duration,
        'top_10_client_error': top_10_client_error,
        'top_10_server_error': top_10_server_error
    }

    # create file for results and put data into it
    try:
        with open(out_file, 'w+') as out:
            json.dump(result, out, indent=2)
    except Exception as write_exc:
        sys.exit(f'Unable to write file because of error - {write_exc}')


def read_dir(log_dir):
    """

    Parameters
    ----------
    log_dir : str
        Path to directory with logs files to parse.

    Returns
    -------
    Write results to files in json format. One result file for each log file in directory.

    """

    # iterate over files in dir
    if os.path.exists(log_dir):
        if os.path.isdir(log_dir):

            files = os.listdir(log_dir)
            for file in files:

                f_name = file.split('.')[0]

                # check that file is log file
                if file.endswith('.log'):
                    read_file(os.path.join(log_dir, file), f'result_{f_name}.json')

        else:
            sys.exit(f'{log_dir} - is not directory')
    else:
        sys.exit(f'{log_dir} - no such directory exists')


def main():
    """Application entry point."""
    args = get_args()

    if args.log_dir:
        read_dir(args.log_dir)
    else:
        read_file(args.log_file, out_file='result.json')


if __name__ == '__main__':

    main()
