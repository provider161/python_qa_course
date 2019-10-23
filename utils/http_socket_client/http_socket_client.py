"""
HTTP client implemented by python socket library, accepts method, url, host, headers.
Returns response text, status code, headers
"""

import socket
import ssl

# arguments for HTTP request
args = {
    'method': 'GET',
    'port': 443,
    'host': 'www.google.com',
    'headers': 'accept: text/html\naccept-language: en-US'
}


def print_response(method: str, host: str, port: int, headers: str):
    """

    Parameters
    ----------
    method: str
        HTTP request method
    port: int
        port for host
    host: str
        host for request
    headers: dict
        Request headers

    Returns
    -------
    Response response text, status code, headers

    """

    # add ssl certificate
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()

    # create socket client
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = context.wrap_socket(sock, server_hostname=host)

    request = f'{method.upper()} / HTTP/1.1\r\n' + f'Host: {host}\r\n' + f'{headers}\r\n\r\n'

    # connect to server and send request
    sock.connect((host, port))
    sock.send(request.encode())

    print_result(sock)


def print_result(sock: socket):
    """
    Get all data returned by response

    Parameters
    ----------
    sock
        socket connection instance
    Returns
    -------
        received data from socket

    """

    BUFF_SIZE = 4096
    data = sock.recv(BUFF_SIZE)
    while len(data) > 0:
        print(data)
        data = sock.recv(BUFF_SIZE)


def main():
    """Application entry point."""

    print_response(method=args['method'], host=args['host'], port=int(args['port']), headers=args['headers'])


if __name__ == '__main__':

    main()
