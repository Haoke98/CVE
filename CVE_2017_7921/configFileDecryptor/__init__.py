# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2022/8/7
@Software: PyCharm
@disc:
======================================="""
from .decryptor import xore, decrypt, strings


def guess(configurationFile: str, username: str) -> list[str]:
    xor = xore(decrypt(open(configurationFile, 'rb').read()))
    result_list = strings(xor.decode('ISO-8859-1'))
    password_list: list[str] = []
    for i, v in enumerate(result_list):
        if v == username:
            password_list.append(result_list[i + 1])
    return password_list
