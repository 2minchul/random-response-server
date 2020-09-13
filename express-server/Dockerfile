FROM node:alpine

COPY package*.json ./
RUN rpm install
COPY app.js ./

CMD ["npm", "start"]
