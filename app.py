
#from logging import exception
#import sys
from flask import Flask

#import sys
#from housing.logger import logging
#from housing.exception import HousingException
#from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])
def index():
    #try:
     #   raise Exception("We are testing custom exception")
    #except Exception as e:
     #   raise HousingException(e,sys) from e
      # logging.info("We are testing logging module")
   return "Starting Machine Learning Projects-- "
    




    #logging.info("We are testing logging modules")

if __name__=="__main__":
    app.run(debug= True)

