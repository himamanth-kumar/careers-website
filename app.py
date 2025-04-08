from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Namaste , I am Himamanth kumar from India"

print("Starting Flask application...")
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)