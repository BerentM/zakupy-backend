run:
	go run pkg/main.go serve --http=0.0.0.0:8001

downgrade:
	go run pkg/main.go migrate down

new migration:
	go run pkg/main.go migrate create $(name)

migrate:
	go run main.go migrate collections
