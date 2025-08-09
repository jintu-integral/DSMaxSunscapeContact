from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv('residents.csv')
        residents = df.to_dict(orient='records')
    except Exception as e:
        residents = []
    return render_template('index.html', residents=residents)

if __name__ == '__main__':
    app.run(debug=True)
