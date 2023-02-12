from datetime import datetime
from datetime import timezone
import csv
import sys
import argparse

def main(config):
    # airhamlogのCSVファイル
    csv_file = open(config['csv_filepath'], encoding="utf_8")
    # 自局コールサイン
    my_callsign = config['my_callsign']
    # 無線機
    rig = config['rig']
    # アンテナ
    anntena = config['anntena']
    f = csv.DictReader(csv_file,
                       delimiter=",",
                       doublequote=True,
                       lineterminator="\r\n",
                       quotechar='"',
                       skipinitialspace=True)
    #出力ファイルを開く
    with open(f"export2daredemoQSL.csv",
                'w', newline='', encoding="utf_8") as expFile:
        writer = csv.DictWriter(expFile, 
            fieldnames=[
                'No',
                '自局コールサイン',
                '相手局コールサイン',
                '交信時刻(YYYY-MM-DD HH:MM:00)',
                '日付のみ保持(有効:1 / 無効:0)',
                'RSTレポート',
                '運用バンド',
                'モード',
                '自局QTH',
                '無線機',
                'アンテナ',
                'オペレーター',
                '相手局QTH',
                'メッセージ',
            ], quoting=csv.QUOTE_ALL)
        writer.writeheader()        
        #No用のカウンタ
        noCnt: int = 1
        #1行分の処理
        for row in f:
            #行オブジェクト
            writeRowObj = {
                'No': noCnt,
                '自局コールサイン': my_callsign,
                '相手局コールサイン':row['callsign'],
                '交信時刻(YYYY-MM-DD HH:MM:00)':datetime.strptime(
                    row['qso_at'],
                    '%Y-%m-%d %H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S'),
                '日付のみ保持(有効:1 / 無効:0)': 0,
                'RSTレポート': row['sent_rst'],
                '運用バンド': row['frequency'],
                'モード': row['mode'],
                '自局QTH': '',
                '無線機': rig,
                'アンテナ' :anntena,
                'オペレーター': '',
                '相手局QTH': '',
                'メッセージ': row['card_remarks'],
            }
            writer.writerow(writeRowObj)
            noCnt += 1

    return 0


def cli():
    parser = argparse.ArgumentParser(
        description='Airhamlog CSV to DaredemoQSL CSV Converter')
    # CSVファイルパス
    parser.add_argument('csv_filepath')
    # 自局コールサイン
    parser.add_argument('my_callsign')
    # 無線機(省略可能)
    parser.add_argument('--rig', required=False, default='')
    # アンテナ(省略可能)
    parser.add_argument('--anntena', required=False, default='')
    args = parser.parse_args()
    return main(vars(args))


if __name__ == '__main__':
    sys.exit(cli())
