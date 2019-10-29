"""
Script prints info about host system, net ports, statistic
"""

import os
import sys
import subprocess
import argparse
import json


def get_args():
    """Arguments parser"""
    args = argparse.ArgumentParser()

    args.add_argument('--package', type=str, action='store', help='Package name to show version')
    args.add_argument('--dir', type=str, action='store',  help='Directory to show files it contains', default='/')
    args.add_argument('--port', type=str, action='store',  help="Port number to show it's type", default='22')

    return args.parse_args()


def get_os_info():
    """
    Gather information about host system, network interfaces and statistic.
    :return:
        os_info - Dict with gathered data
    """
    args = get_args()

    try:
        package_version = subprocess.check_output(f'pip3 freeze | grep {args.package}', shell=True).decode().strip()
    except subprocess.CalledProcessError as e:
        package_version = f'Unable to load package version because of error - {e}'

    try:
        network_interfaces = subprocess.check_output(['netstat', '-i']).decode()
    except subprocess.CalledProcessError as e:
        network_interfaces = f'Unable to load network interfaces because of error - {e}'

    try:
        cpu_info = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).decode()
    except subprocess.CalledProcessError as e:
        cpu_info = f'Unable to load network interfaces because of error - {e}'

    try:
        all_processes = subprocess.check_output(['ps', 'aux']).decode()
    except subprocess.CalledProcessError as e:
        all_processes = f'Unable to load network interfaces because of error - {e}'

    try:
        port_type = subprocess.check_output(f'lsof -nP -iTCP -sTCP:LISTEN | grep :{args.port}', shell=True).decode()
    except subprocess.CalledProcessError as e:
        port_type = f'Unable to load port type because of error - {e}'

    try:
        interfaces_stat = subprocess.check_output('ifconfig').decode()
    except subprocess.CalledProcessError as e:
        interfaces_stat = f'Unable to load interfaces statistic because of error - {e}'

    try:
        cron_status = subprocess.check_output(['systemctl', 'status', 'cron']).decode()
    except subprocess.CalledProcessError as e:
        cron_status = f'Unable to load cron status because of error - {e}'

    os_info = {
        'current_directory': os.getcwd(),
        'os_information': os.uname(),
        'python_core': sys.version,
        'files_list': os.listdir(args.dir),
        'package_version': package_version,
        'default_path': os.getenv('PATH'),
        'network_interfaces': network_interfaces,
        'cpu_info': cpu_info,
        'process_id': os.getpid(),
        'all_processes': all_processes,
        'port_type': port_type,
        'interfaces_stat': interfaces_stat,
        'cron_status': cron_status
    }

    print(json.dumps(os_info, indent=4))


if __name__ == '__main__':
    get_os_info()
