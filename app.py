from flask import Flask, render_template, request, flash
import geohandler
import update
import os
import subprocess


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/help", methods=['POST', 'GET'])
def greeter():
	
	##Get User Location
	if request.headers.getlist("X-Forwarded-For"):
		iip = request.headers.getlist("X-Forwarded-For")[0]
	else:
		iip = request.remote_addr
	ur = update.getIpLoc(iip)
	print("-------------UR----------",ur)	
	m=""
	for t in ur:
		m+=str(t)[0:7]	
		m+=" "	
	##Get Nearest Hospital Name and Coordinates	

	hr = geohandler.getNearestHospitals(ur[0],ur[1])
	hname = hr[0][0]
	hlat = hr[0][1]	
	hlng = hr[0][2]


	##Get Hospital Route
	rr = geohandler.getRouteDistance(ur[0],ur[1],hr[0][1],hr[0][2])

	flash("Your Location : "+m)
	print("Test")
	#discordbot.Alert(ur)
	flash("Nearest Hospital : "+hname)
	flash("Hospital Coordinates : "+str(hlat)[0:7]+' '+ str(hlng)[0:7])
	flash("Distance : "+str(rr[0]))
	flash("Estimated Time for Help To Arrive : " +str(rr[1])+" seconds")
	flash("Alternative Hospitals : "+str(hr[1][0]) + ", " + str(hr[2][0]) + ", " + str(hr[3][0]))
	process = subprocess.Popen(['python', 'discordbot.py',str(ur[0]),str(ur[1])])
	return render_template("help.html",lat1 = str(ur[0]),lon1 = str(ur[1]),lat2 = str(hlat), lon2 = str(hlng))



#Initialize page
if __name__ ==  '__main__':
    
    app.run(debug=True)
    