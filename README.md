# DIC GraduationTask 卒業制作

タイトル　チャットボット＆不動産価格予測<br>
制作日時　2021/10/30<br>
制作期間　10日

## ・なぜこの制作物を作ったのか？
**前職で中古不動産の仕入れ営業を行なっていた時の非効率に感じていた課題を解決する目的**<br>
<br>
具体的に、毎月50〜60件の価格査定を、都度データ収集して査定を行なっていたが、<br>
ほとんどが見込みの低い案件で査定が増えても成約率が上がらない、かつ過去データの<br>
有効利用ができてない事に疑問を感じていた。そこで、自社Webサイトなどに査定依頼の<br>
応対を行ってくれるチャットボットを作り、受注、査定、回答を行ってくれれば見込みの<br>
高い案件に営業が注力でき、業務効率化になるのでは？と思い制作した。<br>

## ・卒業制作としての目標
**上記の課題を解決する為には、Web制作の知識などが必要となるが、**<br>
**DICでは学習していないため今回は目標を簡略化する**<br><br>
卒業制作としては機械学習を用いて、チャットボットと価格予測モデルの2パターンを実装する。<br>

1.チャットボット -Chatbot-<br>
　・会話が成り立つレベルを目指す
<br>
　・対話モデルができあがれば、Replyに応答するTwitterBOTとしてデプロイ
<br>
　・TwitterBOTは、HerokuSchedulerで定期的にreplyする設定まで行う
<br>


2.価格予測 -HousePricePrediction-<br>
　・マンション限定で、少ない入力値（特徴量）で良い精度を目指す
<br>
　・任意の入力値に対して予測できるよう、Flaskで簡単なWebアプリにする

<br>

## ・開発環境/使用言語
|チャットボット|     |
|------------|------------|
| 使用言語|Python … NLP（Janome）,Seq2Seq, Pytorch|
|        |TwitterAPI, Heroku（HerokuScheduler）|
| 開発環境|GoogleColab(GPU), VScode|
| データ  |不動産会社各社のQ＆Aデータ 5,000件|
|        |用語集などの専門用語データ5,000件|
|        |名大コーパス(日常対話データ)15,000件|
|        |TwitterAPI不動産関係のTweet,Reply500,000件|

|価格予測モデル|     |
|------------|------------|
| 使用言語|Python … LightGBM(optuna), Flask|
| 開発環境|GoogleColab(GPU), VScode|
| データ  |47都道府県のマンション取引事例………600,000件|
 　※データ件数は約

<br>

------------------------------------------------------------------------------

<br>

## ・制作データ

### 1. チャットボット -ChatBot-

- twitter_bot
<br>
　-tw_bot.py …メインの処理　!!このファイルをTwitterBOTとしてデプロイ!!
<br>
　-keys.py  … TwitterKeyを保存するため
<br>
　-model_bot.pth …学習したモデル（Pytorch Seq2Seq）
<br>
　-reply_field.pkl  … replyデータ（入力文）
<br>
　-input_field.pkl  … inputデータ（応答文）
<br>
　-runtime.txt  … 
<br>
　-requirements.txt  … ライブラリのバージョンを定義
<br>
　-Procfile  … Heroku用で実行するためのファイル
<br>
<br>


### 2. 不動産価格予測モデル -HousePricePrediction 

- house-price
<br>
　-app.py …メインの処理　!!このファイルをターミナルで実行する!!
<br>
　-data_conversion.py  …入力データをモデルで推定するために変換する処理


- pickle
<br>
　-lgbm_model.pickle …学習済みのLightGBMモデル(Booster)
<br>
　-dict_city_code.pickle  …都道府県のデータを入力したdictデータ

- csv
<br>
　-公営の借家数.csv
<br>
　-転入_転出csv.csv
<br>
　-House.csv
<br>
　-nikkei_stock_average_monthly_jp.csv
<br>
　  ※csvやdict_city_code.pickleはdata_converstion.pyの中で使用する

- templates
<br>
　-index.html   入力画面などを映したフロントのメインデータ
<br>
　-result.html  判定（実行）後の画面データ





