# airhamlog2daredemoqsl
AirHamlogからエクスポートできるCSVファイルを誰でもQSL登録用のCSVに変換するツール

## 必要環境
- pyhtonスクリプトです。python実行環境が必要です。

## できること
- AirHamlog( https://air-hamlog.com/ )からCSV出力したファイルを使って、だれでもQSL( https://fqsl.jp/ )のCSV登録用CSVを作成します。

### CSV項目対応表

|だれでもQSLのCSV項目|対応するAirHamlogCSV項目名|備考|
|---|---|---|
|No|-|1から始まる連番が入ります。|
|自局コールサイン|-|ツール実行時に指定します。|
|相手局コールサイン|callsign||
|交信時刻(YYYY-MM-DD HH:MM:00)|qso_at||
|日付のみ保持(有効:1 / 無効:0)|-|0固定です。|
|RSTレポート|sent_rst||
|運用バンド|frequency||
|モード|mode||
|自局QTH|-|AirHamlog側に項目（sent_qth）は存在しますが、連携しません。|
|無線機|-|ツール実行時に指定できます（任意）|
|アンテナ|-|ツール実行時に指定できます（任意）|
|オペレーター|-||
|相手局QTH|-|AirHamlog側に項目（received_qth）は存在しますが、連携しません。|
|メッセージ|card_remarks||

## 使い方

```shell
$python airhamlog2daredemoqsl.py airhamlog_csv_file YOUR_CALLSIGN [--rig RIG_NAME] [--anntena ANNTENA_NAME]
```
- コマンド例
```shell
$python airhamlog2daredemoqsl.py airhamlog_20230212105022.csv JK1IAT --rig ID-52 --anntena SRH-770
```
