from flask import Flask, render_template
app = Flask(__name__)

#Each HTML page should have links to the other two pages (don't use Jinja here yet).
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def about_me():
    return render_template("portfolio.html")

@app.route("/about")
def portfolio():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()