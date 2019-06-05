from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('chooseCategory.html')

@app.route("/sendCategory", methods=["POST"])
def sendCateg():
  choice = request.form.get('options')
  args = ["python", "gen_recomen.py", choice]
  subprocess.Popen(args)
  return render_template('wait.html')
    
if __name__ == "__main__":
    app.run(debug=True)