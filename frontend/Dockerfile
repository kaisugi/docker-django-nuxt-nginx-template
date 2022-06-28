FROM node:16-slim
ARG AXIOS_BASEURL
ARG AXIOS_BROWSER_BASEURL
RUN apt-get update
WORKDIR /usr/src/app
COPY package.json ./
COPY yarn.lock ./
COPY .yarnrc ./
RUN yarn install
COPY . .
RUN yarn build
ENV HOST=0.0.0.0
