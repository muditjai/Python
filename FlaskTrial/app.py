from flask import Flask, jsonify, request
from Distribution.VedicCityNames import NameTranslator

app = Flask(__name__)


@app.route("/cities")
def get_all_city_names():
    translator = NameTranslator()
    return jsonify(translator.get_all_available_cities())


app.run(port=5000)
