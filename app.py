import json

from flask import Flask, request
import easyocr

app = Flask(__name__)


#pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ocr',methods=['POST'])
def extract_data():
    obj = {}
    if(request.is_json):
        print('Entrou um arquivo')
        obj = request.get_json()
    else:
        obj = request.get_data()
        print('entrou um json')

    reader = easyocr.Reader(['pt'], gpu=False)
    objText = reader.readtext(obj, detail=0,paragraph=True)

    return json.dumps(objText)


if __name__ == '__main__':
    app.run()
