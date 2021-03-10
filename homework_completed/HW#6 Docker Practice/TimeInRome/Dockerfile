FROM ubuntu:16.04
ENV TZ 'Europe/Rome'
RUN echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y tzdata
RUN dpkg-reconfigure tzdata
CMD ["date"]
