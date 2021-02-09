# Docker-books

## Deployment 

Commands:


```bash
docker build -t docker_books .

docker run -d -p80:8000 docker_books
```

## Usage

- To check the server is running:

http://localhost

- To get the catalog:

http://localhost/api/v1/resources/books/all

- To get the books of author Jo Walton:

[http://localhost/api/v1/resources/books?author=Jo Walton](http://localhost/api/v1/resources/books?author=Jo%20Walton)

- To get books published in 2000:

http://localhost/api/v1/resources/books?published=2000

