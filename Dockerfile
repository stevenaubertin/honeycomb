# Use an official Python runtime as a base image
FROM python:3-alpine

# Set arguments
ARG BUILD_DATE
ARG VCS_REF
ARG PROJECT_NAME
ARG PORT=5000
ARG DESCRIPTION
ARG VERSION
ARG VCS_URL

# Set some envirronement variables
ENV PORT=$PORT
ENV HOST=0.0.0.1
ENV LOG_FILENAME="app.log"

# Set labels (see https://microbadger.com/labels)
LABEL maintainer="stevenaubertin@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name=$PROJECT_NAME \
      org.label-schema.description=$DESCRIPTION \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

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