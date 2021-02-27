# Bookflix Micro-services

## Launch all services 
```
docker-compose up -d
```

## Check services state
```
docker-compose logs -f
```

## Stop all services
```
docker-compose stop
```

## Remove all containers (Services)
```
docker-compose down
```


# Exemples (if you want to test on Postman)

Check if `Books service` works
```
http://localhost
```

Check if `Notes service` works
```
http://localhost:8080
```

Check if `Comments service` works
```
http://localhost:5001/api
```

Check if `User auth service` works
```
http://localhost:5000/api
```

For more details of how to use each service, please check the README file present in each service.





