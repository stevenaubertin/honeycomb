# Use an official Python runtime as a base image
FROM python:3-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# The files least likely to be changed should be in lower layers,
# while the files most likely to change should be added last.
COPY ../requirements.txt /app/
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]