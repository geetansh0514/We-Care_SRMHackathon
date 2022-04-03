from flask import Flask, render_template
import geohandler

app = Flask(__name__)

@app.route('/')
def index():
    a = geohandler.getNearestHospitals()
    b = geohandler.getUserLoc()
    op = str(a)
    a = " "
    for j in op:
        a+=str(j)   
    
    return(str(a))

if __name__ == "__main__":
    app.run(debug=True)