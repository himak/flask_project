from blog import app

if __name__ == "__main__":
	debug = False
	host = "0.0.0.0"
	app.run(host, port=5000, debug=True)