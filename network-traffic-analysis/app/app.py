from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<h2>Demo Login (Lab Only)</h2>
<form method="POST">
  <input name="username" placeholder="username"><br><br>
  <input name="password" type="password" placeholder="password"><br><br>
  <button type="submit">Login</button>
</form>
<p>{{ msg }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")
        if u == "admin" and p == "test123":
            msg = "Login successful"
        else:
            msg = "Invalid credentials"
    return render_template_string(PAGE, msg=msg)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
