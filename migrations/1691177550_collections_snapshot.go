package migrations

import (
	"encoding/json"

	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	m "github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models"
)

func init() {
	m.Register(func(db dbx.Builder) error {
		jsonData := `[
			{
				"id": "_pb_users_auth_",
				"created": "2023-08-04 10:00:35.971Z",
				"updated": "2023-08-04 10:00:35.972Z",
				"name": "users",
				"type": "auth",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "users_name",
						"name": "name",
						"type": "text",
						"required": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "users_avatar",
						"name": "avatar",
						"type": "file",
						"required": false,
						"unique": false,
						"options": {
							"maxSelect": 1,
							"maxSize": 5242880,
							"mimeTypes": [
								"image/jpeg",
								"image/png",
								"image/svg+xml",
								"image/gif",
								"image/webp"
							],
							"thumbs": null,
							"protected": false
						}
					}
				],
				"indexes": [],
				"listRule": "id = @request.auth.id",
				"viewRule": "id = @request.auth.id",
				"createRule": "",
				"updateRule": "id = @request.auth.id",
				"deleteRule": "id = @request.auth.id",
				"options": {
					"allowEmailAuth": true,
					"allowOAuth2Auth": true,
					"allowUsernameAuth": true,
					"exceptEmailDomains": null,
					"manageRule": null,
					"minPasswordLength": 8,
					"onlyEmailDomains": null,
					"requireEmail": false
				}
			},
			{
				"id": "zsxmvpv1eprye2g",
				"created": "2023-08-04 19:07:18.162Z",
				"updated": "2023-08-04 19:07:18.162Z",
				"name": "shops",
				"type": "base",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "vgbn5ol1",
						"name": "name",
						"type": "text",
						"required": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					}
				],
				"indexes": [
					"CREATE UNIQUE INDEX ` + "`" + `idx_cbBuTjm` + "`" + ` ON ` + "`" + `shops` + "`" + ` (` + "`" + `name` + "`" + `)"
				],
				"listRule": null,
				"viewRule": null,
				"createRule": null,
				"updateRule": null,
				"deleteRule": null,
				"options": {}
			},
			{
				"id": "a496t5ecicy1ggl",
				"created": "2023-08-04 19:08:16.462Z",
				"updated": "2023-08-04 19:08:16.462Z",
				"name": "categories",
				"type": "base",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "zvm7tfsd",
						"name": "name",
						"type": "text",
						"required": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					}
				],
				"indexes": [
					"CREATE UNIQUE INDEX ` + "`" + `idx_x3hHJUc` + "`" + ` ON ` + "`" + `categories` + "`" + ` (` + "`" + `name` + "`" + `)"
				],
				"listRule": null,
				"viewRule": null,
				"createRule": null,
				"updateRule": null,
				"deleteRule": null,
				"options": {}
			},
			{
				"id": "kad2uv2kdosxck6",
				"created": "2023-08-04 19:11:24.254Z",
				"updated": "2023-08-04 19:28:10.819Z",
				"name": "products",
				"type": "base",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "hkvpeaqu",
						"name": "name",
						"type": "text",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "3dplny0e",
						"name": "shop_id",
						"type": "relation",
						"required": false,
						"unique": false,
						"options": {
							"collectionId": "zsxmvpv1eprye2g",
							"cascadeDelete": false,
							"minSelect": null,
							"maxSelect": 1,
							"displayFields": [
								"name"
							]
						}
					},
					{
						"system": false,
						"id": "n3lcx3en",
						"name": "category_id",
						"type": "relation",
						"required": false,
						"unique": false,
						"options": {
							"collectionId": "a496t5ecicy1ggl",
							"cascadeDelete": false,
							"minSelect": null,
							"maxSelect": 1,
							"displayFields": [
								"name"
							]
						}
					},
					{
						"system": false,
						"id": "rotwnbmf",
						"name": "current_amount",
						"type": "number",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null
						}
					},
					{
						"system": false,
						"id": "zmprqdmg",
						"name": "target_amount",
						"type": "number",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null
						}
					}
				],
				"indexes": [
					"CREATE UNIQUE INDEX ` + "`" + `idx_b0B6EK0` + "`" + ` ON ` + "`" + `products` + "`" + ` (` + "`" + `category_id` + "`" + `)"
				],
				"listRule": null,
				"viewRule": null,
				"createRule": null,
				"updateRule": null,
				"deleteRule": null,
				"options": {}
			},
			{
				"id": "ope3rlxn7i03wgc",
				"created": "2023-08-04 19:20:54.056Z",
				"updated": "2023-08-04 19:32:15.344Z",
				"name": "shopping_list",
				"type": "view",
				"system": false,
				"schema": [
					{
						"system": false,
						"id": "9jcmybos",
						"name": "name",
						"type": "text",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "4uxydtwa",
						"name": "shop",
						"type": "text",
						"required": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "iozx9ych",
						"name": "category",
						"type": "text",
						"required": false,
						"unique": false,
						"options": {
							"min": null,
							"max": null,
							"pattern": ""
						}
					},
					{
						"system": false,
						"id": "v68s6odb",
						"name": "current_amount",
						"type": "number",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null
						}
					},
					{
						"system": false,
						"id": "7g6cdsni",
						"name": "target_amount",
						"type": "number",
						"required": true,
						"unique": false,
						"options": {
							"min": null,
							"max": null
						}
					},
					{
						"system": false,
						"id": "jjllkyjv",
						"name": "missing_amount",
						"type": "json",
						"required": false,
						"unique": false,
						"options": {}
					}
				],
				"indexes": [],
				"listRule": null,
				"viewRule": null,
				"createRule": null,
				"updateRule": null,
				"deleteRule": null,
				"options": {
					"query": "SELECT \n  p.id, \n  p.name,\n  s.name as shop, \n  c.name as category,\n  p.current_amount, \n  p.target_amount, \n  (p.target_amount - p.current_amount) as missing_amount\nFROM products p\nLEFT JOIN shops s on s.id = p.shop_id\nLEFT JOIN categories c on c.id = p.category_id\nWHERE p.target_amount - p.current_amount > 0"
				}
			}
		]`

		collections := []*models.Collection{}
		if err := json.Unmarshal([]byte(jsonData), &collections); err != nil {
			return err
		}

		return daos.New(db).ImportCollections(collections, true, nil)
	}, func(db dbx.Builder) error {
		return nil
	})
}
