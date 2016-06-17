FROM ubuntu
RUN apt-get update
RUN apt-get -y install make && apt-get -y install g++
RUN apt-get -y install gsl-bin && apt-get -y install libgsl0-dev
COPY karambola-src karambola-src
WORKDIR karambola-src
RUN make clean
RUN make