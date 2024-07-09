import requests
import base64
import json
import os

def Main():
    # 'Imgsetting.json' ファイルを開き、内容を読み込みます
    with open('Imgsetting.json') as f:
        Imgsetting = json.load(f)
    
    # HTTP POSTリクエストを送信し、レスポンスを受け取ります
    resp = requests.post(url='http://localhost:7860/sdapi/v1/txt2img', json=Imgsetting)
    
    # レスポンスのJSONデータを取得します
    response_json = resp.json()
    
    # 画像データを取得し、デコードします
    imgdata = response_json["images"][0]
    
    # 出力ディレクトリをチェックし、存在しない場合は作成します
    output_dir = "temp"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 画像データをファイルに書き込みます
    with open(os.path.join(output_dir, "output.png"), "wb") as f:
        buf = base64.b64decode(imgdata)
        f.write(buf)

    return

if __name__ == '__main__':
    Main()
