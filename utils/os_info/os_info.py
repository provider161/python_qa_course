"""
Script prints info about host system, net ports, statistic
"""

import os, sys, subprocess, argparse, json


def get_args():
    """Arguments parser"""
    args = argparse.ArgumentParser()

    args.add_argument('--package', type=str, action='store', help='Package name to show version')
    args.add_argument('--dir', type=str, action='store',  help='Directory to show files it contains', default='/')

    return args.parse_args()


def get_os_info():
    args = get_args()

    files_in_dir = os.listdir(args.dir)

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

    os_info ={
        'current_directory': os.getcwd(),
        'os_information': os.uname(),
        'python_core': sys.version,
        'files_list': files_in_dir,
        'package_version': package_version,
        'default_path': os.getenv('PATH'),
        'network_interfaces': network_interfaces,
        'cpu_info': cpu_info,
        'process_id': os.getpid(),
        'all_processes': all_processes
    }

    print(json.dumps(os_info, indent=4))


get_os_info()
