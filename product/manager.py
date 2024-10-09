import click

from main import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)


# Thêm lệnh migrate vào Flask CLI
@app.cli.command("db")
def db_command():
    """Lệnh này có thể chạy các lệnh di trú database (database migrations)."""
    click.echo("Lệnh migrate của bạn được tích hợp qua Flask CLI")
