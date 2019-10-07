This is a simple web access logs parser.

Overview:

    It accepts log file path or path to directory with logs and generates result file with following data:
    - count of all request types, count of each request type
    - top 10 ip addresses which request came form
    - top 10 ip addresses which request had longest duration
    - top 10 ip addresses with client error status (4**)
    - top 10 ip addresses with server error status (5**)

Parameters:

    --log-dir - path to directory with logs

    --log-file - path to log file

Output:

    Script generates json file with results. If provided path to log file, generates 'result.json' file.
    If provided path to directory, generates 'result_*log_filename*.json' file for each log

Usage:

    Run in your command line:

        python3 log_parser.py --log-dir='path/to/logs/directory' - to parse all logs in specific directory

        python3 log_parser.py --log-file='path/to/logs/file' - to parse specific log file