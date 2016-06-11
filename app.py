from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    topic = request.form['query']
    return render_template('results.html', topic=topic)

if __name__ == '__main__':
  app.run(debug=True)
