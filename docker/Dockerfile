FROM amazonlinux:2.0.20200722.0

LABEL maintainer="nicola-piccolo"

RUN yum update -y
RUN yum install -y shadow-utils
RUN yum install -y python3

RUN useradd -m ml-environment-template

ENV HOME_DIRECTORY="/home/ml-environment-template"
ENV LOGS_DIRECTORY="$HOME_DIRECTORY/logs"
RUN mkdir $LOGS_DIRECTORY
ENV VIRTUAL_ENV="$HOME_DIRECTORY/ml-environment-template-venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR $HOME_DIRECTORY
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src ./
COPY docker/prodBootstrap.sh .
RUN chown -R ml-environment-template:ml-environment-template $HOME_DIRECTORY
USER ml-environment-template

EXPOSE 8000

ENTRYPOINT ["sh", "prodBootstrap.sh"]