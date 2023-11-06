# るいざ・しゃーろっと シナリオ集

井の頭公園の無頼派エルフ、るいざ・しゃーろっとによる演劇や映画のシナリオ

## 必要なもの

1. [Python 3.12](https://www.python.org/downloads/)
2. [Git](https://git-scm.com/)
3. ここのリポジトリのファイル

## 使い方

1. Python 3.12とGitをインストール
   1. このとき環境変数Pathを設定しておくこと
2. Gitでこのファイル一式を展開する
   1. コマンドラインの場合: `git clone https://github.com/huidetang/LouisaScenario.git`
   2. Visual Studio Codeなどを使ってもOK
3. コマンドラインで `pip install poetry` を実行
4. 展開したディレクトリで以下のコマンドを順番に実行する
   1. `poetry install`
   2. `poetry exec python make_pdf.py`（PDF作成）もしくは`poetry exec python make_html.py`（HTML作成）

なお、別のシナリオを変換する際にはそれぞれのPythonファイルの4行目にある`.fountain`のファイル名を書き換えること。

## 記法

[satamame](https://github.com/satamame)さんによる[日本式Fountain](https://satamame.github.io/pscn/fountain/for_japanese.html)で書かれている。

## 脚本リスト

- `yuki.fountain`: ぜんぶ、雪のせいだ ※ wip
  - [https://www.pixiv.net/novel/show.php?id=20084173](原作小説: ぜんぶ、雪のせいだ)

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/huidetang/LouisaScenario">るいざ・しゃーろっと シナリオ集</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://lit.link/VRCLouisa">るいざ・しゃーろっと</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
