#pip install flask pypng pyqrcode

from flask import Flask, jsonify, request, abort
from QRGen import GenerateQR

app = Flask(__name__)


@app.route("/test",methods=["GET","POST"])
def test():
    if request.method == "GET":
        return abort(404)

    elif request.method == "POST":
        url = request.json["url"]
        GenerateQR(web_address=url)

        #name = request.json['name']
        return jsonify({"response":f"QR Code Generated for {url} & saved at QR_Images"})



if __name__ == "__main__":

    app.run(debug=True)
