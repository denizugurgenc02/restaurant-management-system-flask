from flaskr import create_app

config_name = "development"
app = create_app(config_name=config_name)


@app.cli.command("init-db")
def init_db_command():
    with app.app_context():
        from flaskr.core.extensions import db

        db.create_all()

    print("Successfully created tables")


if __name__ == "__main__":
    app.run()
