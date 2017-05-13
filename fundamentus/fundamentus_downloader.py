import requests
import sys

BASE_URL = "http://fundamentus.com.br/"

def get_stocks():
    with open("fundamentus.txt", "r") as fundamentus_file:
        stocks = fundamentus_file.read().split()
    return stocks

def download_all(stocks, session_id):
    for stock in stocks:
        url = "{}balancos.php?papel={}&tipo=1".format(BASE_URL, stock)
        requests.get(url)

        download_link = "{}planilhas.php?SID={}".format(BASE_URL, session_id)
        stock_file = requests.get(download_link)

        with open("./{}".format(stock), 'wb') as f:
            print("Downloading {} ...".format(stock))
            for chunk in stock_file.iter_content(chunk_size=128):
                f.write(chunk)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage example: python fundamentus_downloader.py e81tphr617q54")
    else:
        session_id = sys.argv[1]
        stocks = get_stocks()
        download_all(stocks, session_id)
