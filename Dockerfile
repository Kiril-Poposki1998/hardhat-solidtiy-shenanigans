FROM node:18.20.6

WORKDIR /app

COPY . .

RUN npm install
RUN npm install ganache

CMD ["npx", "ganache"]
