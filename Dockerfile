# Start from a ubuntu Docker image
FROM ubuntu:kinetic

# Install python3
RUN apt-get update && apt-get install -y python3.9

# Set workdir
WORKDIR /usr/src/app

# Copy all of the source code
COPY . .

# Execute the script
ENTRYPOINT ["python3", "caesar.py"]