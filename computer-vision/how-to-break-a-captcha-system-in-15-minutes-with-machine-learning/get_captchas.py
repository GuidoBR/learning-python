import sys
import argparse
import requests

URL = "https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/fnsforms/zvn/zvnCaptchaImg/1513594000956?sessionID=1f150c4a-861e-4672-a572-0ad5e694e597_20171218114639841"
BASEDIR = 'trainning_captcha/{}.png'

def get_image(filenumber):
    resp = requests.get(URL)
    file_name = BASEDIR.format(filenumber)
    with open(file_name, 'wb') as img:
        written = img.write(resp.content)
    return written, file_name


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('number', help="Number of files")
    args = argparser.parse_args()
    n = int(args.number)
    print('Downloading {} CAPTCHA images...'.format(n))
    for i in range(10000,n):
        get_image(i)
        print("File {}.png saved".format(i))
