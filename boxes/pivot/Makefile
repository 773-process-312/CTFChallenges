build:
	docker build -t repo.treescale.com/bhorn/boot2root-pivot .

run: build
	docker run -it -p 3000:3000 -p 1337:1337 repo.treescale.com/bhorn/boot2root-pivot

push: build
	docker push repo.treescale.com/bhorn/boot2root-pivot
