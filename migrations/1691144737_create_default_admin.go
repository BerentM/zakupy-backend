package migrations

import (
	"os"

	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	"github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models"
)

func init() {
	migrations.Register(func(db dbx.Builder) error {
		// up
		dao := daos.New(db)
		admin := &models.Admin{}
		admin.Email = os.Getenv("ADMIN_EMAIL")
		err := admin.SetPassword(os.Getenv("ADMIN_PASSWORD"))
		if err != nil {
			return err
		}
		return dao.SaveAdmin(admin)
	}, func(db dbx.Builder) error {
		// down
		dao := daos.New(db)
		admin, _ := dao.FindAdminByEmail(os.Getenv("ADMIN_EMAIL"))
		if admin != nil {
			return dao.DeleteAdmin(admin)
		}
		return nil
	})
}
