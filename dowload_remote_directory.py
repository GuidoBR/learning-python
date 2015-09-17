import requests
from lxml import html


def main():
    fs = Filesystem()
    print(fs)
    fs.download_all()


class Filesystem(object):
    def __init__(self):
        self.url = 'http://192.168.0.15:8000'
        self.items = self._list_objects()

    def __repr__(self):
        return 'Filesystem(%s)' % (self.url)

    def __str__(self):
        return 'URL %s has %d items.' % (self.url, len(self))

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def _list_objects(self):
        r = requests.get(self.url)
        tree = html.fromstring(r.text)
        files_elements = tree.xpath('/html/body/ul/li')
        return [filename.text_content().rstrip() for filename in files_elements]

    def _download(self, filename):
        r = requests.get(self.url + '/' + filename, stream=True)
        print('Downloading %s' % filename)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return filename

    def download_all(self):
        map(self._download, self.items)


class File(Filesystem):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.items = [item for item in self.items if not item.endswith('/')]


class Directory(Filesystem):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.items = [item for item in self.items if item.endswith('/')]
