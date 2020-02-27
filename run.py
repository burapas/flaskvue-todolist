import os
import click
from app import create_app, db
from app.models import Todo

# create the application instance    
app = create_app(os.getenv("FLASK_ENV"))


@app.cli.command("initdb")
def initdb():
    click.echo("Initializing database...")
    with db.database:
        db.database.create_tables([Todo], fail_silently=True)

@app.cli.command("tests")
def tests():
    click.echo("Running tests...")
    import pytest
    pytest.main([])


if __name__ == '__main__':
    app.run()