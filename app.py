from flask import Flask, render_template
import random
import cleanup
import markov

# connect to the webwith unique name
app = Flask(__name__)


@app.route('/')
def main():
    words = cleanup.text_list('text/dickens.txt')
    m_chain = markov.order_mchain(2, words)
    c_start = markov.start_token(m_chain)
    walk_the_dog = markov.walk(c_start, m_chain)
    almost = markov.finalize(walk_the_dog)
    home = str(almost)
    return render_template("main.html", sentence = home)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
