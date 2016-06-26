from flask import Flask, render_template, request
import wikiscrape
import json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    topic = request.form['query'].strip()
    data = wikiscrape.topic_search(topic)
    summary = wikiscrape.summary(topic)
    return render_template('base.html', data=data, summary=summary)

@app.route("/subtopic", methods=["POST", "GET"])
def add_subtopic():
    topic = request.args.get('topic')
    data = wikiscrape.topic_search(topic)
    return json.dumps(data)


if __name__ == '__main__':
  app.run(debug=True)
