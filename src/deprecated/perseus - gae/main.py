import random
import webapp2

from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.ext import webapp


class CmdModel(db.Model):
	mode = db.StringProperty()
	param = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add=True)
	
class SensorModel(db.Model):
	batt = db.StringProperty()
	nw = db.StringProperty()
	gyroX = db.StringProperty()
	gyroY = db.StringProperty()
	gyroZ = db.StringProperty()
	compass = db.StringProperty()
	temp = db.StringProperty()
	humidity = db.StringProperty()
	pressure = db.StringProperty()
	lat = db.StringProperty()
	lon = db.StringProperty()
	alt = db.StringProperty()
	ir1 = db.StringProperty()
	ir2 = db.StringProperty()
	sonar = db.StringProperty()
	date = db.DateTimeProperty(auto_now_add=True)

class ImageModel(db.Model):
	image = db.BlobProperty()
	date = db.DateTimeProperty(auto_now_add=True)

class sensorRead(webapp2.RequestHandler):
	def get(self):
		sensorModel = db.GqlQuery("SELECT * FROM SensorModel ORDER BY date DESC").fetch(1)
		for currentModel in sensorModel :
			batt = currentModel.batt
			nw = currentModel.nw
			gyroX = currentModel.gyroX
			gyroY = currentModel.gyroY
			gyroZ = currentModel.gyroZ
			compass = currentModel.compass
			temp = currentModel.temp
			humidity = currentModel.humidity
			pressure = currentModel.pressure
			lat = currentModel.lat
			lon = currentModel.lon
			alt = currentModel.alt
			ir1 = currentModel.ir1
			ir2 = currentModel.ir2
			sonar = currentModel.sonar
			json = "{\n\t\"BATTERY\":"+str(batt)+",\n\t\"NETWORK\":\""+str(nw)+"\",\n\t\"GYROX\":"+str(gyroX)+",\n\t\"GYROY\":"+str(gyroY)+",\n\t\"GYROZ\":"+str(gyroZ)+",\n\t\"COMPASS\":"+str(compass)+",\n\t\"TEMPERATURE\":"+str(temp)+",\n\t\"HUMIDITY\":"+str(humidity)+",\n\t\"PRESSURE\":"+str(pressure)+",\n\t\"LATITUDE\":"+str(lat)+",\n\t\"LONGITUDE\":"+str(lon)+",\n\t\"ALTITUDE\":"+str(alt)+",\n\t\"IR1\":"+str(ir1)+",\n\t\"IR2\":"+str(ir2)+",\n\t\"SONAR\":"+str(sonar)+"\n}"
			self.response.out.write(json)

class sensorWrite(webapp2.RequestHandler):
	def post(self):
		sensorModel = SensorModel()
		sensorModel.batt = self.request.get('batt')
		sensorModel.nw = self.request.get('nw')
		sensorModel.gyroX = self.request.get('gyroX')
		sensorModel.gyroY = self.request.get('gyroY')
		sensorModel.gyroZ = self.request.get('gyroZ')
		sensorModel.compass = self.request.get('compass')
		sensorModel.temp = self.request.get('temp')
		sensorModel.humidity = self.request.get('humidity')
		sensorModel.pressure = self.request.get('pressure')
		sensorModel.lat = self.request.get('lat')
		sensorModel.lon = self.request.get('lon')
		sensorModel.alt = self.request.get('alt')
		sensorModel.ir1 = self.request.get('ir1')
		sensorModel.ir2 = self.request.get('ir2')
		sensorModel.sonar = self.request.get('sonar')
		sensorModel.put()
		self.response.out.write("OK")

class cmdRead(webapp2.RequestHandler):
	def get(self):
		cmdModel = db.GqlQuery("SELECT * FROM CmdModel ORDER BY date DESC").fetch(1)
		for currentModel in cmdModel :
			mode = currentModel.mode
			param = currentModel.param
			date = currentModel.date
			string = str(mode)+"\n"+str(param)+"\n"+str(date)
			self.response.out.write(string)
			
class cmdWrite(webapp2.RequestHandler):
	def post(self):
		cmdModel = CmdModel()
		cmdModel.mode = self.request.get('mode')
		cmdModel.param = self.request.get('param')
		cmdModel.put()
		self.response.out.write("OK")

class imageWrite(webapp2.RequestHandler):
	def post(self):
		imageModel = ImageModel()
		imageModel.image=db.Blob(str(self.request.get('image')))
		imageModel.put()
		self.response.out.write("OK")

class imageRead(webapp2.RequestHandler):
	def get(self):
		imageModel = db.GqlQuery("SELECT * FROM ImageModel ORDER BY date DESC").fetch(1)
		for currentModel in imageModel:
			img = currentModel.image		
			self.response.out.write("data:image/jpeg;base64,"+img)
			return
		self.response.out.write("./lib/img.jpg")

class initialize(webapp2.RequestHandler):
	def post(self):
		self.response.out.write("OK")

app = webapp2.WSGIApplication([('/readSensor', sensorRead),
			('/writeSensor', sensorWrite),
			('/writeImage', imageWrite),
			('/readImage', imageRead),
			('/writeCmd', cmdWrite),
			('/readCmd', cmdRead),
			('/init',initialize)],
			debug=True)
