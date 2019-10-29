FROM python:3.7

# install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# install ChromeDriver
RUN /bin/bash -c "wget -N http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip -P /"
RUN unzip /chromedriver_linux64.zip
RUN rm /chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin


# install python requirements
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN rm requirements.txt

# clone tests code
RUN git clone https://github.com/provider161/python_qa_course.git

CMD /bin/bash