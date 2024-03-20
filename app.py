from flask import Flask
import flask
from flask import request
import searcher
from makeurl import makeURL
app = Flask(__name__)

@app.route("/")
def proliferation():
    return flask.render_template('home.html')

@app.route("/results", methods=["POST"])
def search():
    dtitles = searcher.search(request.form['query'], 5)
    otitles =  []
    for key in dtitles:
        otitles.append(key)
    if dtitles != "error":
        if len(otitles) == 1:
            return flask.render_template("results.html", searchQuery= request.form['query'], title1=otitles[0], url1=makeURL(dtitles[otitles[0]]), title2=" ", url2=" ", title3=" ",url3=" ", title4=" ",url4=" ", title5=" ", url5=" ")
        elif len(otitles) == 2:
            return flask.render_template("results.html", searchQuery= request.form['query'], title1=otitles[0], url1=makeURL(dtitles[otitles[0]]), title2=otitles[1], url2=makeURL(dtitles[otitles[1]]), title3=" ", url3=" ", title4=" ", url4 = " ", title5=" ", url5=" ")
        elif len(otitles) == 3:
            return flask.render_template("results.html", searchQuery= request.form['query'], title1=otitles[0], url1=makeURL(dtitles[otitles[0]]), title2=otitles[1], url2=makeURL(dtitles[otitles[1]]), title3=otitles[2], url3=makeURL(dtitles[otitles[2]]), title4=" ", url4 = " ", title5=" ", url5=" ")
        elif len(otitles) == 4:
            return flask.render_template("results.html", searchQuery= request.form['query'], title1=otitles[0], url1=makeURL(dtitles[otitles[0]]), title2=otitles[1],url2=makeURL(dtitles[otitles[1]]), title3=otitles[2], url3=makeURL(dtitles[otitles[2]]), title4=otitles[3], url4=makeURL(dtitles[otitles[3]]), title5=" ", url5 = " ")
        elif len(otitles) == 5:
            return flask.render_template("results.html", searchQuery= request.form['query'], title1=otitles[0], url1=makeURL(dtitles[otitles[0]]), title2=otitles[1], url2=makeURL(dtitles[otitles[1]]), title3=otitles[2], url3=makeURL(dtitles[otitles[2]]), title4=otitles[3], url4=makeURL(dtitles[otitles[3]]), title5=otitles[4], url5=makeURL(dtitles[otitles[4]]))
    else:
        return("An error occurred. Please try again.")

if __name__ == '__main__':
    app.run()