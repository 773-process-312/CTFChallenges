build:
	docker build -t repo.treescale.com/bhorn/boot2root-writable .

run: build
	docker run -it -p 8000:8000 -p 2244:22 -p 6379:6379 repo.treescale.com/bhorn/boot2root-writable

push: build
	docker push repo.treescale.com/bhorn/boot2root-writable
