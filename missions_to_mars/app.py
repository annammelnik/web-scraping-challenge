from flask import Flask, render_template, redirect
import pymongo
import scrape_marss

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.marsmission
col = db.mars

@app.route("/")
def home():
    mars_data = col.find_one()
    return render_template('index.html',mars=mars_data)

@app.route('/scrape')
def scrape():
    mars_data = scrape_marss.scrape()
    #col.update_one({}, {"$set": mars_data}, upsert=True)
    col.insert_one(mars_data)

    return "Got the data!"



if __name__ == "__main__":
    app.run(debug=True)