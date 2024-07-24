# get_setting

設定ファイルが記載された json から目的のデータを取得するPythonライブラリ

## Install

```bash
python -m pip install　git+https://github.com/Torahugu1/get_setting.git
```

## Usage

```python
from get_setting import get_setting
# ただしstrの場合相対パスはsettings.json基準で絶対パスに書き換えられる。
filePathName = get_setting("filePath", "./settings.json")
setting_dict = get_setting("abc", "./settings.json")
```
