from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    data = request.get_json()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("donnees.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}]\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("\n" + "-" * 30 + "\n\n")

    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(debug=True)
