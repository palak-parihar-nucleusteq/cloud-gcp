FROM node:20-bullseye-slim

RUN apt update -y && apt install -y openjdk-11-jdk bash

RUN npm install -g firebase-tools

# Expose any necessary ports
EXPOSE 9005

COPY . .

RUN npm --prefix ./functions install

RUN echo '#!/bin/sh \n firebase emulators:start' > ./entrypoint.sh && \
    chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]