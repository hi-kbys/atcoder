FROM nikolaik/python-nodejs

# install atcoder-cli
RUN apt-get -y update \ 
    && apt-get -y upgrade \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install chromium-driver \
    && npm install -g atcoder-cli

# install requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt