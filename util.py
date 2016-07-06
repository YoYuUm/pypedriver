

import re


def urljoin(*pieces):
    return '/'.join(s.strip('/') for s in pieces)


def clean(string):
    return re.sub('\W|^(?=\d)', '_', string)
