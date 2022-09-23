# syntax = docker/dockerfile:1.2

# Use slim buster images
FROM python:3.8.5-slim-buster

LABEL version="0.0.1"

# Disable auto-cleanup after install:
RUN rm /etc/apt/apt.conf.d/docker-clean

# Install updates and cache across builds
ENV DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/apt,id=apt apt-get update && apt-get -y upgrade

# Create user and work dir
RUN useradd --create-home app

USER app
WORKDIR /home/app/mac_address
RUN mkdir --parents /home/app/mac_address

# Install python requirements
COPY --chown=app:app ./requirements.txt ./
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/home/app/.cache/pip,id=pip pip install -r requirements.txt

# Copy the source code
COPY --chown=app:app . ./

# Run
ENTRYPOINT [ "./run.sh" ]

