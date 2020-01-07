FROM python:latest
MAINTAINER Ali Akbar Arbisoft

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app

#ENV PHANTOM_JS "phantomjs-1.9.8-linux-x86_64"
#RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \
#  && tar xvjf $PHANTOM_JS.tar.bz2 \
#  && mv $PHANTOM_JS /usr/local/share \
#  && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

#RUN apt-get update -y \
#  && apt-get -y install google-chrome-stable \
#  && apt-get install -y unzip xvfb libxi6 libgconf-2-4 \
#  && wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip \
#  && unzip chromedriver_linux64.zip \
#  && mv chromedriver /usr/bin/chromedriver \
#  && chown root:root /usr/bin/chromedriver \
#  && chmod +x /usr/bin/chromedriver

# Gecko Driver
#ENV GECKODRIVER_VERSION 0.26.0
#RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
#  && rm -rf /opt/geckodriver \
#  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
#  && rm /tmp/geckodriver.tar.gz \
#  && mv /opt/geckodriver /usr/local/bin/geckodriver-$GECKODRIVER_VERSION \
#  && chmod 755 /usr/local/bin/geckodriver-$GECKODRIVER_VERSION \
#  && ln -fs /usr/local/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
#  && ln -fs /usr/local/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires

#ENV PATH=$PATH:/usr/bin/

ENV SELENIUM_BROWSER=firefox
ENV SELENIUM_HOST=selenium-hub
ENV SELENIUM_PORT=4444
