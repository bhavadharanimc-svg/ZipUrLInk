from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)
database.init_db()

@app.route("/")
def home():
    urls = database.get_all_urls()
    return render_template("index.html", urls=urls)

@app.route("/shorten", methods=["POST"])
def shorten():
    original_url = request.form["url"]
    short_code = database.generate_short_code(original_url)
    database.save_url(original_url, short_code)
    short_url = f"http://127.0.0.1:5000/{short_code}"
    urls = database.get_all_urls()
    return render_template("index.html", short_url=short_url, urls=urls)

@app.route("/<short_code>")
def redirect_url(short_code):
    original_url = database.get_original_url(short_code)
    if original_url:
        database.increment_clicks(short_code)
        return redirect(original_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)