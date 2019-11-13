def celsFromFahr(fahr):
	cels = (fahr - 32) * 5 / 9
	return cels

def fahrFromCels(cels):
	fahr = cels * 9 / 5 + 32
	return fahr

def mphFromKph(kph):
	mph = kph * 0.621371
	return mph

def windChillMetric(tempC, windKPH):
	pow = windKPH ** 0.16
	chill = 13.12 + 0.6215 * tempC - 11.37 * pow + 0.3965 * tempC * pow
	return chill

def windChillUS(tempF, windMPH):
	pow = windMPH ** 0.16
	chill = 35.74 + 0.6215 * tempF - 35.75 * pow + 0.4275 * tempF * pow
	return chill

def main():
	c = 20
	f = fahrFromCels(c)
	print(c)
	print(f)
	print(celsFromFahr(f))

	c = -20
	v = 5
	print(round(windChillMetric(c, v), 1))
	print(round(celsFromFahr(windChillUS(fahrFromCels(c), mphFromKph(v))), 1))

if __name__ == "__main__":
	main()
