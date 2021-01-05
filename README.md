# PYMAZE
![tests](https://github.com/OkanoShinri/dev-tutorial-exercise/workflows/tests/badge.svg)


自動生成される迷路に、実際に迷い込んでみよう。



## インストール方法
インストールコマンドは`make install`です。
permission errorが出る場合は`sudo make install`を入力してください。

## 遊び方
pythonパッケージとしてつくられています。
Python Consoleを開いて以下のように入力してください。
```py
>>> from pymaze.pymaze import pymaze
>>> pymaze()
```

### オプション
pymaze関数には引数として迷路の縦横サイズを渡すことができます。
デフォルトでは縦横ともに31となっています。
引数は**7以上の奇数**である必要があります。
```py
pymaze(15,27)
```

## アンインストール方法
アンインストールコマンドは`make uninstall`です。


## 困ったことがあったら
https://github.com/OkanoShinri/dev-tutorial-exercise/issues
上のissuesに書き込んでください。


