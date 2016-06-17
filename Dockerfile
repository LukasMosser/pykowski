FROM ubuntu
RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get -y install make && apt-get -y install g++
RUN apt-get -y install gsl-bin && apt-get -y install libgsl0-dev
RUN apt-get install -y python python-dev python-distribute python-pip
RUN apt-get -y install git
COPY karambola-src karambola-src
WORKDIR karambola-src
RUN make clean
RUN make
WORKDIR /
RUN git clone https://github.com/LukasMosser/pykowski.git
RUN pip install -r /pykowski/requirements.txt
RUN pip install tifffile
WORKDIR /pykowski
