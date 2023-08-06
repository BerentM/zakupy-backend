package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	_ "zakupy_backend/migrations"

	"github.com/labstack/echo/v5"
	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
	"github.com/pocketbase/pocketbase/plugins/migratecmd"
)

func main() {
	app := pocketbase.New()

	isGoRun := strings.HasPrefix(os.Args[0], os.TempDir())
	migratecmd.MustRegister(app, app.RootCmd, migratecmd.Config{
		// enable auto creation of migration files when making collection changes in the Admin UI
		Automigrate: isGoRun,
	})

	// serves static files from the provided public dir (if exists)
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
		return nil
	})

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		// register new "GET /hello" route
		e.Router.GET("/hello", func(c echo.Context) error {
			z := 2 + 2
			return c.String(200, fmt.Sprintf("Hello world! %v", z))
		}, apis.ActivityLogger(app), apis.RequireGuestOnly())

		return nil
	})

	if err := app.Start(); err != nil {
		log.Fatal(err)
	}
}
