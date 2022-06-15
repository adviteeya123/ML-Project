
from flask import Flask

app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])
def index():
    return "Starting Machine Learning Projects-- Kya ho raha hai khushbu bhot ladai karte ho -- Kya ho raha hai swati bhot thak jati ho tum kaam karte karte karte ho -- Kya ho raha hai jyoti  bhot gym jane lage ho aur wahan ladai  karte ho "

if __name__=="__main__":
    app.run(debug= True)

