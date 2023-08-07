run:
	go run pkg/main.go serve --http=0.0.0.0:8001

build:
	go build -o build/zakupyBackend -a pkg/main.go

downgrade:
	go run pkg/main.go migrate down

new migration:
	go run pkg/main.go migrate create $(name)

migrate:
	go run pkg/main.go migrate collections

sync:
	go run pkg/main.go migrate history-sync
