FROM node:alpine

COPY package*.json ./
RUN npm install
COPY app.js ./

CMD ["npm", "start"]
