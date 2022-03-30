# PYMAZE

自動生成される迷路に、実際に迷い込んでみよう。

![img01](https://user-images.githubusercontent.com/72956592/103644547-e37ad280-4f99-11eb-841f-8afa114277e4.png)

![pymaze_demo](https://user-images.githubusercontent.com/72956592/160869261-21192be5-0223-4303-a72a-568b49a2fc2e.gif)

## 遊び方

仮想環境を作って、その中で遊ぶのが良いでしょう。

```sh
make venv
```

手早く遊びたいときは、make venv してから

```sh
make run
```

ですぐに遊ぶことができます。デフォルトでは縦横ともに 31 のサイズの迷路が生成されます。

迷路のサイズを指定したいときは、コマンドラインで引数を渡してください。引数は**7 以上の奇数**である必要があります。

```sh
venv/bin/python3 src/pymaze.py --width 15 --height 17 --process
```

`--process`を付けると、迷路の生成過程を可視化できます。`--width`は`-w`、`--height`は`-hi`と省略することもできます。

### インストール

pymaze は python パッケージとしてインストールすることもできます。
`make install`(エラーが出る場合は`sudo make install`)を打ってインストールした後、
Python Console を開いて以下のように入力してください。

```py
>>> from pymaze.pymaze import pymaze
>>> pymaze()
```

ここでも引数として迷路の縦横サイズを渡すことができます。

```py
>>> pymaze(15,27)
```

### アンインストール

```sh
make uninstall
```

でアンインストールできます。

## 困ったことがあったら

issues に書き込んでください。
