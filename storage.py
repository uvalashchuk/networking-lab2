import hashlib
import os

STORAGE_PATH = 'storage'
PASSWD_PATH = '.passwd'


def assert_system_file(file: str):
    if file[0] == '.':
        raise PermissionError


def get_for_user(user: str, file: str) -> bytes:
    assert_system_file(file)

    f = open(STORAGE_PATH + '/' + user + '/' + file, 'rb')
    data = f.read()
    f.close()
    return data


def create_for_user(user: str, file: str, data: bytes):
    assert_system_file(file)

    f = open(STORAGE_PATH + '/' + user + '/' + file, 'wb')
    f.write(data)
    f.close()


def delete_for_user(user: str, file: str):
    assert_system_file(file)

    os.remove(STORAGE_PATH + '/' + user + '/' + file)


def authenticate(user: str, passwd: bytes):
    for registered_user in os.listdir(STORAGE_PATH):
        if registered_user == user:
            passwd_f = open(STORAGE_PATH + '/' + user + '/' + PASSWD_PATH, 'r', encoding='utf-8')
            stored_passwd_hash = passwd_f.read()
            passwd_f.close()
            return stored_passwd_hash == hashlib.sha256(passwd).hexdigest()
    return False
