# AWS IoT 1-click Buttonを使ったカエルコール

## 概要

家に帰る前には、家族にカエルコールをしますよね？(うちはします)

古くは電話(だから「コール」)でしたが、これがポケベル、メールなどと時代の変遷と共にその手段は変わってきて最近はLINEを使われるケースが多いのではないでしょうか。

しかし、忙しいとどうしても「帰るね」「今日は遅くなるよ」のたった一言を打つだけも面倒だったり忘れたりします。

そこで、ボタン1クリックでそれを送れれば楽になるのかなと作ったのがこのプロジェクトになります。

ボタンクリックイベントごとに、テキストとCGを組み合わせたメッセージを設定してLINEのグループ等に投稿することができます。

例えばボタンクリックが「帰るね」、ダブルクリックが「急いで帰るね」、ロングクリックが「ごめん、遅くなる」といった感じです。

## 使い方概要

AWSのアカウントの作り方などの詳細は適宜調べてください。

- python2.7をインストールする
- AWSのアカウントを作り、aws cliが動くようにする
- [この辺](https://aws.amazon.com/jp/iot-1-click/devices/)を見てデバイスを入手する
  - 個人的には接続が簡単で電池も変えられる[SORACOM LTE-M Button powered by AWS](https://pages.soracom.jp/LP_SORACOM-LTE-M-Button.html)がお勧めです。
- このプロジェクトをgit cloneする
- serverless frameworkをインストールする
  ```bash
  %pip install serverless
  ```
- 必要なライブラリを入れる
  ```bash
  %pip install -r requirements.txt -t ./
  ```
- クリックしたときにLINEに送られるめっせーじ
- クリックしたときにLINEに送られるCGを3種類準備し、どこかhttpsでアクセスできるところに置き、URLとファイル名をconfig.iniに記載する
- 取りあえずデプロイする
  ```bash
  %sls deploy
  ```
- LINE Messaging APIのDeveloper Trial(無償)を契約してボットアカウントを作る
- デプロイ時に表示されたAPI GatewayのURLを、Messaging APIのコールバックに登録する
- ボットアカウントとLINEで友達になり、適当なグループを作成してそこに招待する
- AWSのコンソールから、Lambda関数「kaeru-call-hello-dev」のCloudWatch Logsを見るとグループ招待のイベントログが出てるはずなので「groupId」の部分を取得してconfig.iniに記載する
- sls
- もう1回デプロイする
  ```bash
  %sls deploy
  ```
- ボタンをひもづける
  - AWSのコンソールないしはCLIで、作成されたLambda関数「kaeru-call-sendmsg-dev」にボタンをひもづける


 
