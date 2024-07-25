#!/usr/bin/env python3
'''json形式の設定ファイルを読み込み

Usage
-----
import get_setting
configDict = get_setting.get_setting("config","./settings.json")
'''
from typing import Any
import json
from pathlib import Path


SETTINGLIKE = str | int | float | dict[str, str | int | float] | None


def get_setting(keyname: str, set_json_name: str | Path = "./settings.json") -> SETTINGLIKE:
    """settings.jsonファイルから辞書型の設定を出力する。
    設定の中のパスが相対パスの場合は「set_json_nameのディレクトリからの相対パス」として\n
    絶対パスに変換する。
    ただし、相対パスとみなされる文字列は'.'で始まり'/'が含まれるものである。

    Parameters
    ----------
    keyname : str
        読み込みたい設定のキー
    set_json_name : str | Path
        settings.jsonのパス。デフォルトはカレントディレクトリのsettings.jsonから取得する。

    Returns
    -------
    configure : SETTINGLIKE
        設定
    """
    set_json_name = Path(set_json_name)
    set_json_dirname = Path(set_json_name).parent
    with set_json_name.open(encoding="utf-8") as jsonf:
        setDict: dict[str, Any] = json.load(jsonf)
    if keyname not in setDict:
        print("設定ファイルに"+keyname+"はありません。")
        return None
    configure: SETTINGLIKE = setDict[keyname]

    configure = AbsPathInDict(configure, set_json_dirname)
    return configure


def AbsPathInDict(configDict: Any, dirName: Path) -> Any:
    """dictのstrのパス表記を「dirNameの相対パス」から絶対パスに変換する\n
    相対パスとみなされる文字列は'.'で始まり'/'が含まれるものである
    """
    if isinstance(configDict, float | int):
        pass
    if isinstance(configDict, str):
        if configDict.startswith('.') and ('/' in configDict):
            configDict = str(dirName / configDict)
    if isinstance(configDict, dict):
        for key in configDict.keys():
            configDict[key] = AbsPathInDict(configDict[key], dirName)
    return configDict
