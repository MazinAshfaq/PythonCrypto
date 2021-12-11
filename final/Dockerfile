# Use the Python version of alpine as the base image
FROM python:3.7-slim-stretch as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

# Specify your e-mail address as the maintainer of the container image
MAINTAINER Your Name "ashfaq@pdx.edu"	

FROM base

COPY --from=builder /install /usr/local

# Copy the contents of the current directory into the container directory /app

COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN pip install --no-cache -r requirements.txt


# Set the program that is invoked upon container instantiation
ENTRYPOINT ["python"]

# Set the parameters to the program
CMD gunicorn --bind :$PORT --workers 1 --threads 8 app:app
