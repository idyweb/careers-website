from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
       "id": 1,
       "title": "Data Analyst",
       "location": "Uyo, Nigeria",
       "salary": "NGN 1,000,000"
       
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Abuja, Nigeria",
        "salary": "NGN 12,000,000"
    },
    {
        "id": 3,
        "title": "Frontend Developer",
        "location": "Remote",
        "salary": "NGN 500,000"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Remote",
        "salary": "NGN 800,000"
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html', jobs= JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)