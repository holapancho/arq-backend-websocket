run with 
uvicorn main:app --reload   

docker build -t web-socket .

docker run -p 0.0.0.0:80:8090 web-socket

ws://host.docker.internal:8090/ws