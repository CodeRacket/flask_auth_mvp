import click

def register_commands(app):
    @app.cli.command("test")
    def hello():
        click.echo("Hello, World!")
