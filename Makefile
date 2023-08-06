run:
	go run pkg/main.go serve --http=0.0.0.0:8001

build:
	go build -o build/zakupy_backend -a pkg/main.go

downgrade:
	go run pkg/main.go migrate down

new migration:
	go run pkg/main.go migrate create $(name)

migrate:
	go run pkg/main.go migrate collections
