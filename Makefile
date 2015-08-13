.PHONY : build run

build:
	docker build -t facemash .

run:
	docker run -p 8889:80 facemash
