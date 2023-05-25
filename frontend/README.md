# Single page app using FastAPI and Vue.js
This project is a single page app using FastAPI and Vue.js. The app is a simple list of people, where you can add, edit and delete people (CRUD operations). The app is using a mongoDB database to store the data. 

Both the backend and frontend is implemented and running in docker containers.

## Built with
- FastAPI
- Vue.js
- mongoDB

## Getting started
1. Clone the repo
```
git clone https://github.com/computas/fastapi-vue.git
```
2. Navigate to the project folder
```
cd fastapi-vue
```
3. Build and run the docker containers
```
docker-compose up -d --build
```

## Usage
The app is running on http://localhost:80. The API is running on http://localhost:8000, you can check the API documentation on http://localhost:8000/docs. The mongoDB database is running on port `27017`.
