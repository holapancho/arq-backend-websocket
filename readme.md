run with 
uvicorn main:app --reload   

docker build -t web-socket .

docker run --rm  -p 0.0.0.0:8090:80 web-socket

ws://host.docker.internal:8090/ws