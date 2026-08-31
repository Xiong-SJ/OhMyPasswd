#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/8/24 09:39
# @Author  : YISHI
# @Email   : wowoxiongsj123123@outlook.com
# @File    : processors.py
# @Software: PyCharm

# 标准库导入
import json

# 第三方库导入
from pypinyin import pinyin, lazy_pinyin, Style

# 本地模块导入
# from utils import helper


class PersonInfo:
    def __init__(
        self,
        name: str | None = None,
        phone_numbers: str | list | None = None,
        identity: str | None = None,
        birthdate: str | list | None = None,
        hometowns: str | list | None = None,
        workplaces: str | list | None = None,
        educational_institutions: str | list | None = None,
        accounts: str | list | None = None,
        passwords: str | list | None = None,
    ):

        self.name = name
        self.phone_numbers = phone_numbers
        self.identity = identity
        self.birthdate = birthdate
        self.hometowns = hometowns
        self.workplaces = workplaces
        self.educational_institutions = educational_institutions
        self.accounts = accounts
        self.passwords = passwords

    @classmethod
    def include_json(cls, person_info_json: dict) -> PersonInfo:
        name = person_info_json.get("name", None)
        phone_numbers = person_info_json.get("phone_numbers", None)
        identity =person_info_json.get("identity", None)
        birthdate = person_info_json.get("birthdate", None)
        hometowns = person_info_json.get("hometowns", None)
        workplaces = person_info_json.get("workplaces", None)
        educational_institutions = person_info_json.get(
            "educational_institutions", None
        )
        accounts = person_info_json.get("accounts", None)
        passwords = person_info_json.get("passwords", None)

        return cls(
            name=name,
            phone_numbers=phone_numbers,
            identity=identity,
            birthdate=birthdate,
            hometowns=hometowns,
            workplaces=workplaces,
            educational_institutions=educational_institutions,
            accounts=accounts,
            passwords=passwords,
        )

    @classmethod
    def include_file(cls, path: str) -> PersonInfo | None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return PersonInfo.include_json(data)
        except Exception as e:
            print(e)
            return None


class ParserFuncsRegitry:
    _instance = None
    _funcs = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def regitry(cls, func):
        cls._funcs.append(func.__name__)
        return func

    @classmethod
    def get_funcs_list(cls):
        return cls._funcs.copy()

"""
解析函数的写法:
# 函数名不能重复,重复会返回error
# 参数只能是PersonInfo类
@ParserFuncsRegitry.regitry
def func(name:PersonInfo) -> dict:
    #处理方法
    #返回值必须是dict类型

返回的内容
key: 你在类里面处理值的名称
value: 处理后值的列表

eg:
处理的是ParsonInfo.name
{
    name:['nihao','nihao',...]
}
"""
# 开始你们的操作吧


def parsed_data(data: PersonInfo, parser_funcs_regitry: ParserFuncsRegitry) -> dict|None:
    return None


def main():
    """主函数：程序入口逻辑"""
    pass


if __name__ == "__main__":
    main()
