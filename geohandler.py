import requests
import json
import os

#Functions - getUserLoc() - to 

#alternative methods to get the ip and geolocation

#ip = requests.get('https://api.ipify.org').content.decode('utf8')
#print('My public IP address is: {}'.format(ip))
#ipresponse = requests.get("https://geolocation-db.com/json/{}&position=true".format(ip)).json()
#print(ipresponse)

def getUserLoc():
        
    fresponse = requests.get('https://freegeoip.app/json/').json()
    loc = [fresponse['latitude'],fresponse['longitude'] ]
    return([fresponse['latitude'],fresponse['longitude']])
    
def getNearestHospitals():
    
    fresponse = requests.get('https://freegeoip.app/json/').json()
    loc = [fresponse['latitude'],fresponse['longitude'] ]

    print("Your Current Coordinates are : ",loc[0],loc[1])

    API_KEY = 'xRV3hllT0sjTNaxj2jKTGO22qnYKqA1QDPqQdhFUUvg'
    
    base_url = 'https://discover.search.hereapi.com/v1/discover?at={},{}&q=hospital&apikey='.format(loc[0],loc[1])+API_KEY+'&limit=5'
    response = requests.get(base_url)
    print("\nClosest Hospitals to you \n\n")
    
    rt = []
    for i in range(5):
        print(response.json()['items'][i]['title'],end=" coordinates - ")
        print(response.json()['items'][i]['position'])
        rt.append([response.json()['items'][i]['title'],response.json()['items'][i]['position']['lat'],response.json()['items'][i]['position']['lng']])
    return(rt)
    #print(data)
    
    

a = getNearestHospitals()
print("A",a)

b = getUserLoc()

def getRouteDistance(lat1,lng1,lat2,lng2):
    
    print("Pos 1 ",lat1,lng1," Pos 2",lat2,lng2)
    
    print("Sending Request to : ",r"http://router.project-osrm.org/route/v1/car/{},{};{},{}?overview=false".format(lng1,lat1,lng2,lat2),"\n\n")
    r = requests.get(r"http://router.project-osrm.org/route/v1/car/{},{};{},{}?overview=false".format(lng1,lat1,lng2,lat2))
    print(r)
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    print("Distance in meters : ",route_1['distance'])
    print("Duration to reach there : ",route_1['duration'])
    return(route_1['distance'],route_1['duration'])


getRouteDistance(b[0],b[1],a[0][1],a[0][2])    