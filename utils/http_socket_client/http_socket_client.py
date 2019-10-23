"""
HTTP client implemented by python socket library, accepts method, url, host, headers.
Returns response text, status code, headers
"""

import socket
import ssl
from collections import Counter
from html.parser import HTMLParser

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

    BUFF_SIZE = 4096
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if '</html>' in part.decode():
            break
    return data.decode()


class MyHTMLParser(HTMLParser):

    # Initializing lists
    tags = []
    links = []
    images = []
    text = []

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        # parsing all tags
        self.tags.append(startTag)
        # parsing links
        if startTag == 'a':
            attr = dict(attrs)
            self.links.append(attr['href'])
        # parsing images
        elif startTag == 'img':
            attr = dict(attrs)
            self.images.append(attr['src'])

    def handle_data(self, data):
        # parsing text in tags
        self.text.append(data)


def main():
    """Application entry point."""

    parser = MyHTMLParser()
    html = print_response(method=args['method'], host=args['host'], port=int(args['port']), headers=args['headers'])
    parser.feed(html)
    tags = Counter(parser.tags)
    popular_tag = sorted(Counter(parser.tags).items(), key=lambda k: k[1])
    links = list(parser.links)
    images = list(parser.images)
    text = list(parser.text)
    result = {
        'all_tags': tags,
        'popular_tag': popular_tag[-1],
        'links': links,
        'images': images,
        'text': text
    }

    print('--------All tags----------------------------------------')
    for tag in list(result['all_tags']):
        print(tag)
    print()
    print('--------Most popular tag--------------------------------')
    print(result['popular_tag'])
    print()
    print('--------Links-------------------------------------------')
    for link in result['links']:
        print(link)
    print()
    print('--------Images------------------------------------------')
    for image in result['images']:
        print(image)
    print()
    print('--------Text in tags------------------------------------')
    for t in result['text']:
        print(t)


if __name__ == '__main__':

    main()
