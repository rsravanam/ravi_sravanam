ARG  IMAGE_REPO=sravanam1242/private_docker
ARG  IMAGE_NAME=ubuntu
ARG  IMAGE_VERSION=14.04

#1 our base image
FROM ${IMAGE_REPO}:${IMAGE_NAME}-${IMAGE_VERSION}

#2 Env vars
ENV MESOS_VERSION=1.3.1

#3 Update the packages.
RUN apt-get update

#4 Install a few utility tools.
RUN apt-get install -y tar wget git

#5 Install the latest OpenJDK.
RUN apt-get install -y openjdk-7-jdk

#6 Install autotools (Only necessary if building from git repository).
RUN apt-get install -y autoconf libtool

#7 Install other Mesos dependencies.
RUN apt-get -y install build-essential python-dev python-six python-virtualenv libcurl4-nss-dev libsasl2-dev libsasl2-modules maven libapr1-dev libsvn-dev

#8 Get Mesos Master
RUN wget -O /opt/mesos-${MESOS_VERSION}.tar.gz http://www.apache.org/dist/mesos/${MESOS_VERSION}/mesos-${MESOS_VERSION}.tar.gz

#9 Extract Mesos Master
RUN cd /opt/ && tar -zxf mesos-${MESOS_VERSION}.tar.gz

#10 Run bootstrap file
RUN cd /opt/mesos-${MESOS_VERSION} && ./bootstrap

#11 Configure and build.
RUN cd /opt/mesos-${MESOS_VERSION} && mkdir build && cd build && ../configure && make

#12 Run test suite.
RUN cd /opt/mesos-${MESOS_VERSION}/build && make check

#13 Install (Optional, but checking!!!).
RUN cd /opt/mesos-${MESOS_VERSION}/build && make install	

#14 Create Mesos master work directory exists and has proper permissions
RUN mkdir /var/lib/mesos && chmod 754 /var/lib/mesos

#15 Start Mesos master (ensure work directory exists and has proper permissions).
RUN cd /opt/mesos-${MESOS_VERSION}/build && ./bin/mesos-master.sh --ip=127.0.0.1 --work_dir=/var/lib/mesos

#16 Start Mesos agent (ensure work directory exists and has proper permissions).
RUN cd /opt/mesos-${MESOS_VERSION}/build && ./bin/mesos-agent.sh --master=127.0.0.1:5050 --work_dir=/var/lib/mesos

#17 Run C++ framework (exits after successfully running some tasks).
RUN cd /opt/mesos-${MESOS_VERSION}/build && ./src/test-framework --master=127.0.0.1:5050

#18 Run Java framework (exits after successfully running some tasks).
RUN cd /opt/mesos-${MESOS_VERSION}/build && ./src/examples/java/test-framework 127.0.0.1:5050

#19 Run Python framework (exits after successfully running some tasks).
RUN cd /opt/mesos-${MESOS_VERSION}/build && ./src/examples/python/test-framework 127.0.0.1:5050

