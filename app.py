from flask import Flask, render_template, request, flash
import geohandler
import os
import subprocess


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

##Get User Location
ur = geohandler.getUserLoc()
m = ""
for i in ur:
    m+=str(i)
    m+=" "
    
##Get Nearest Hospital Name and Coordinates

hr = geohandler.getNearestHospitals()
hname = hr[0][0]
hlat = hr[0][1]
hlng = hr[0][2]


##Get Hospital Route
rr = geohandler.getRouteDistance(ur[0],ur[1],hr[0][1],hr[0][2])


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/help", methods=['POST', 'GET'])
def greeter():
	flash("Your Location : "+m)
	print("Test")
	#discordbot.Alert(ur)
	flash("Nearest Hospital : "+hname)
	flash("Hospital Coordinates : "+str(hlat)+" , " + str(hlng))
	flash("Distance : "+str(rr[0]))
	flash("Estimated Time for Help To Arrive : " +str(rr[1])+" seconds")
	flash("Alternative Hospitals : "+str(hr[1][0]) + ", " + str(hr[2][0]) + ", " + str(hr[3][0]))
	process = subprocess.Popen(['python', 'discordbot.py'])	
	return render_template("help.html")
if __name__ ==  '__main__':
    
    app.run(debug=True)
    