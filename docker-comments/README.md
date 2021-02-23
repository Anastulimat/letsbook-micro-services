# Docker

## Build docker
>docker build -t comments .

## Run docker container (Attached mode)
>docker run -it -p 5001:5001 comments

## Run docker container (detached mode)
>docker run -d -p 5001:5001 comments


# Test

## Check if API works
>http://localhost:5001/api


## Check if database connection works by retrieving data
##### Here 2 is stands for book_id
>http://localhost:5001/api/comments/2


