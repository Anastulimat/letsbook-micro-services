# Docker-books

## Deployment 

Commands:


```bash
docker build -t docker_notes .

docker run -d -p8080:8080 docker_notes
```

## Usage

- To check the server is running:

http://localhost:8080

- To get all notes on all books:

http://localhost:8080/api/v1/resources/notes/all

- To get the notes of user 1:

http://localhost:8080/api/v1/resources/notes?user_id=1

- To get notes on book 2:

http://localhost:8080/api/v1/resources/notes?book_id=2

- To add a note: send a POST request to

http://localhost:8080/api/v1/resources/add/

with the following fields inside the request (all of them being mandatory): `user_id`, `book_id`, `note`.
