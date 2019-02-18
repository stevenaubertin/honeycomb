# Use an official Python runtime as a base image
FROM python:3-alpine

#--------------------------- Set Arguments
# Environnement
ARG PROJECT_NAME='Honeycomb'
ARG CONFIG_ENV="config.DevelopmentConfig"
# Api
ARG TITLE=$PROJECT_NAME
ARG VERSION
ARG DESCRIPTION
# Web Server
ARG HOST=0.0.0.0
ARG PORT=5000
# Source Control
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE
# Logger
ARG LOG_FILENAME="app.log"

#--------------------------- Set Environment variables
# Environnement
ENV CONFIG_ENV=$CONFIG_ENV
# Api
ENV TITLE=$TITLE
ENV VERSION=$VERSION
ENV DESCRIPTION=$DESCRIPTION
# Web Server
ENV PORT=$PORT
ENV HOST=$HOST
# Logger
ENV LOG_FILENAME=$LOG_FILENAME

#--------------------------- Set Labels (see https://microbadger.com/labels)
LABEL maintainer="stevenaubertin@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name=$PROJECT_NAME \
      org.label-schema.description=$DESCRIPTION \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

#-------------------------------- Set Source
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# The files least likely to be changed should be in lower layers,
# while the files most likely to change should be added last.
COPY /src/* /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE $PORT

# Run app.py when the container launches
CMD ["python", "app.py"]