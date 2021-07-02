import requests



def download(img, download_dir='.'):
    response = requests.get(img)

    if response.status_code != 200:
        raise requests.RequestException(
            f'Response Status from Img Downloader did not return 200. Returned: {response.status_code}')

    content = response.content

    file_name = get_name(img)
    file_name = download_dir + '/' + file_name
    file = open(file_name, 'wb')
    file.write(content)
    file.close()


def get_name(img):
    return img.split('/')[-1]


if __name__ == '__main__':
    img = 'https://ggsc.s3.amazonaws.com/images/uploads/The_Science-Backed_Benefits_of_Being_a_Dog_Owner.jpg'
    download(img)
