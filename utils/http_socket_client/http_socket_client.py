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


def get_response(method: str, host: str, port: int, headers: str) -> str:
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

    request = f'{method.upper()} / HTTP/1.1\n\n' + f'Host: {host}\n\n' + f'{headers}'

    # connect to server and send request
    sock.connect((host, port))
    sock.send(request.encode())
    result = sock.recv(8192)

    return result.decode()


def main():
    """Application entry point."""

    result = get_response(method=args['method'], host=args['host'], port=int(args['port']), headers=args['headers'])
    print(result)


if __name__ == '__main__':

    main()
