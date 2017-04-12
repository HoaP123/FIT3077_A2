class location:
    # @hoa: this class contains the temperature and rainfall of a certain area.
    def __init__(self, name, date, time, temp, rainfall):
        self.locationname = name
        self.date = date
        self.time = time
        self.temp = temp
        self.rainfall = rainfall

    # @hoa: returns the location name, date and time as one string.
    def getLocation_date_time(self):
        return self.locationname + " " + self.date + " " + self.time

    # @hoa: returns the location name of the object.
    def getLocation(self):
        return self.locationname

    # @hoa: returns the date the weather information was taken.
    def getDate(self):
        return self.date

    # @hoa: returns the time the weather information was taken.
    def getTime(self):
        return self.time

    # @hoa: returns the temperature of the location.
    def getTemp(self):
        return self.temp

    # @hoa: returns the rainfall levels of the location.
    def getRainfall(self):
        return self.rainfall

    def __str__(self):
        return self.getLocation_date_time() + '\n' + "Temperature: " + self.temp + '\n' + "Rainfall: " + self.rainfall

    # @hoa: TEST
    def serialize(self):
        return {
            'locationName': self.locationname,
            'date': self.date,
            'time': self.time,
            'temperature': self.temp,
            'rainfallLevel': self.rainfall
        }