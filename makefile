geckodriver:
	wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
	tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
	rm geckodriver-v0.26.0-linux64.tar.gz
	sudo mv geckodriver /usr/local/bin/
	chmod 755 /usr/local/bin/geckodriver
