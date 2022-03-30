# PYMAZE

自動生成される迷路に、実際に迷い込んでみよう。

![img01](https://user-images.githubusercontent.com/72956592/103644547-e37ad280-4f99-11eb-841f-8afa114277e4.png)

## インストール方法

インストールコマンドは`make install`です。
permission error が出る場合は`sudo make install`を入力してください。

## 遊び方

python パッケージとしてつくられています。
Python Console を開いて以下のように入力してください。

```py
>>> from pymaze.pymaze import pymaze
>>> pymaze()
```

### オプション

pymaze 関数には引数として迷路の縦横サイズを渡すことができます。
デフォルトでは縦横ともに 31 となっています。
引数は**7 以上の奇数**である必要があります。

```py
pymaze(15,27)
```

## アンインストール方法

アンインストールコマンドは`make uninstall`です。

## 困ったことがあったら

issues に書き込んでください。
