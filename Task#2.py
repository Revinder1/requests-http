import requests
import os
from pprint import pprint


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, path_on_computer: str):
        href_dict = self.get_upload_link(disk_file_path=disk_file_path)
        href = href_dict.get('href')
        response = requests.put(href, data=open(path_on_computer, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл успешно загружен'


if __name__ == '__main__':
    TOKEN = ''
    path_to_file = input('Укажите директорию загружаемого файла: ')
    file_list = os.listdir(path_to_file)
    file_name = input(f'Какой файл из текущей директории Вы хотите загрузить?({", ".join(file_list)}): ')
    # Т.к. я знаю, что файлов не много, сделал вывод списка файла из директории для удобства, так бы убрал
    ya = YaUploader(TOKEN)
    pprint(ya.upload_file_to_disk(f'Netology/{file_name}', rf'{path_to_file}\{file_name}'))
