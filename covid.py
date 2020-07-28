import COVID19Py
covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()
locations = covid19.getLocations(rank_by='recovered')
c=str(input("Enter the country name: "))
location = covid19.getLocationByCountryCode(c)
print(location)