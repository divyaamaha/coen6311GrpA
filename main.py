from flask import Flask, request, render_template
import pymongo
# define the mongodb client
uri = "mongodb://coen6311soft:MAwO1xIVS5ktNeS7IGAE9nrVew9vFEN1d3ePAHLZ7ifJMq6wj5kY1bcBry2e4Qqtvw9b2cBPezQ50zXJK5hr3Q==@coen6311soft.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@coen6311soft@"
client = pymongo.MongoClient(uri)

# define the database to use
db = client['coen6311soft']
# define the flask app
app = Flask(__name__)


# define the home page route
@app.route('/')
def hello_world():
    return render_template("index.html")
# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Name'] = request.form['name']
        data['Email'] = request.form['email']
        data['Age'] = request.form['age']
        data['Gender'] = request.form['gender']
        print(data['Gender'])
        db.studentData.insert_one(data)

    return render_template("index.html")


# start the flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
