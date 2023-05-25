FROM node:lts-alpine as builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM node:lts-alpine

WORKDIR /app

COPY --from=builder /app/dist .

RUN npm install -g http-server

CMD ["http-server", "dist"]
