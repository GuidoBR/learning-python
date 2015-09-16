import requests
from lxml import html

url = 'http://192.168.0.15:8000'


def download(filename):
    r = requests.get(url + '/' + filename, stream=True)
    print('Downloading %s' % filename)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return filename


def list_objects_from_url(url):
    r = requests.get(url)
    tree = html.fromstring(r.text)
    files_elements = tree.xpath('/html/body/ul/li')
    return [filename.text_content().rstrip() for filename in files_elements]


def get_files(objects):
    return [thing for thing in objects if not thing.endswith('/')]


def get_directories(objects):
    return [thing for thing in objects if thing.endswith('/')]


def main():
    objects = list_objects_from_url(url)
    files = get_files(objects)
    map(download, files)
