#
# Phase: Build
#

ARG MARVIN_VERSION
ARG REGISTRY_NAME

FROM golang:1.12.9-alpine3.10 AS builder

# Necessary dependencies
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.10/main" >/etc/apk/repositories
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.10/community" >>/etc/apk/repositories
RUN apk update

RUN apk add bash curl git musl openssh openssh-client gcc build-base

### Application ###

RUN mkdir /app /code

# Copy the code
COPY . /code
WORKDIR /code

# Compile the binary
RUN GOOS=linux GOARCH=amd64 go build -tags static_all -o /app/marvin-dockerfile .

### Toolbox ###

RUN mkdir /toolbox

FROM us.gcr.io/$REGISTRY_NAME/marvin:$MARVIN_VERSION

USER root

# Necessary dependencies
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.10/main" >/etc/apk/repositories
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.10/community" >>/etc/apk/repositories
RUN apk update

RUN apk add bash curl git go build-base musl-dev openssh

# Secure code directory
RUN chmod -R 777 /etc
RUN chmod -R o-rwx /code
RUN useradd -u 1000 runner && mkdir -p /home/runner && chown -R 1000:3000 /home/runner

# Copy the builds
COPY --from=builder /app /app

#
# Phase: Analyzer

# Install hadolint
RUN wget -O /toolbox/hadolint https://github.com/hadolint/hadolint/releases/download/v1.17.2/hadolint-Linux-x86_64
RUN chmod u+x /toolbox/hadolint && chown -R 1000:3000 /toolbox/hadolint

USER 1000
