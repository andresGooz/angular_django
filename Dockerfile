FROM node:15.11.0
RUN mkdir /Angular
WORKDIR /Angular
RUN npm install
RUN npm install -g @angular/cli@11.2.3
RUN npm install --save @angular/material @angular/cdk
RUN npm install --save @angular/animations
COPY . /Angular/
