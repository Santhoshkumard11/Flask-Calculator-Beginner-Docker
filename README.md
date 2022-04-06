# Flask-Calculator-Beginner
This is Beginners Friendly Flask Application which does the basic arithmetic operations (+,-,*,/) 

[Click here check the Docker Hub Repo](https://hub.docker.com/r/santhoshkdhana/flask-calculator-beginner)

## Pull the docker Image
```
docker pull santhoshkdhana/flask-calculator-beginner:latest
```
## Start the container
```
docker container run -d -p 5000:5000 --name=santyflask flask-calculator-beginner
```


# Flask Calculator
The container will expose port **5000**

**API**

POST - /add

POST - /subtract

POST- /multiply

POST- /division

send POST request to the endpoints with a JSON in the body

x is the first variable

y is the second variable

Sample JSON:
```JSON
{
    "x":193,
    "y":657
}
```
Sample Response:
```JSON
{
    "Message": -464,
    "Status Code": 200
}
```
