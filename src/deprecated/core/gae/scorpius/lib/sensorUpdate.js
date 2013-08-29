function updateSensor() {
	sensorUpdate();
}
function sensorUpdate() {
	var request = null;
	if (window.XMLHttpRequest) {
		request = new XMLHttpRequest();
	} else if (window.ActiveXObject) {
		request = new ActiveXObject("Microsoft.XMLHTTP");
	}
	if (request) {
		request.open("GET", './readSensor');
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				json = request.responseText;
				sensorPrint(json);
			}
		}
		request.send(null);
	} 
	else {
		alert("Sorry, you must update your browser before seeing Ajax in action.");
	}
}

function sensorPrint(jsonStr) {
	if(jsonStr!="") {
		var json = eval ("(" + jsonStr + ")");
		$("#sensorViewBattery").html(json.BATTERY);
		$("#sensorViewTemperature").html(json.TEMPERATURE);
		$("#sensorViewCompass").html(json.COMPASS);
		$("#sensorViewAccX").html(json.GYROX);
		$("#sensorViewAccY").html(json.GYROY);
		$("#sensorViewAccZ").html(json.GYROZ);
		$("#sensorViewLatitude").html(json.LATITUDE);
		$("#sensorViewLongitude").html(json.LONGITUDE);
		$("#sensorViewProximity").html(json.PROXIMITY);
		$("#sensorViewIRDown").html(json.IRDOWN);
		$("#sensorViewSonarFront").html(json.SONARFRONT);
		$("#sensorViewSonarLeft").html(json.SONARLEFT);
		$("#sensorViewSonarRight").html(json.SONARRIGHT);

		setCompassDirection(json.COMPASS);		
		
		for(j=0;j<14;j+=1) {
			gyroX[j]=gyroX[j+1];
			gyroY[j]=gyroY[j+1];
			gyroZ[j]=gyroZ[j+1];
		}
		gyroX[14]=json.GYROX;
		gyroY[14]=json.GYROY;
		gyroZ[14]=json.GYROZ;
		setAccelerometerGraph();
	}
	setTimeout(startUpdates,100);
}
