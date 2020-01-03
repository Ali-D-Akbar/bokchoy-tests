FROM python:latest
MAINTAINER Ali Akbar Arbisoft

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app

# Gecko Driver
ENV GECKODRIVER_VERSION 0.26.0
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /usr/local/bin/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /usr/local/bin/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /usr/local/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
  && ln -fs /usr/local/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires

ENV PATH=$PATH:/usr/local/bin/.

ENV SELENIUM_BROWSER=firefox
ENV SELENIUM_HOST=localhost
ENV SELENIUM_PORT=4444
