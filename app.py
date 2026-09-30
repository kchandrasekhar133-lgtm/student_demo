from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        students.append({
            "name": name,
            "age": age,
            "course": course
        })

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
