import click
import faker
from trogon import tui


@tui()
@click.group()
def cli():
    pass


@click.command("generate")
@click.option("-n", "--names", default=0, help="Number of fake names.")
@click.option("-w", "--words", default=0, help="Number of random words.")
@click.option("-e", "--emails", default=0, help="Number of fake email addresses.")
def generate_data(names, words, emails):
    "Generates fake names, random words, and fake email addresses."
    fake = faker.Faker()
    if names:
        fake_names = [fake.name() for _ in range(int(names))]
        click.echo("Fake Names:")
        click.echo("*" * 30)
        click.echo("\n".join(fake_names))
    if words:
        fake_words = [fake.word() for _ in range(int(words))]
        click.echo("\nRandom Words:")
        click.echo("*" * 30)
        click.echo("\n".join(fake_words))
    if emails:
        fake_emails = [fake.email() for _ in range(int(emails))]
        click.echo("\nFake Email Addresses:")
        click.echo("*" * 30)
        click.echo("\n".join(fake_emails))


@click.command("greet")
@click.option("-n", "--name", default="You beautiful", help="Greets a given name")
def hello(name):
    click.echo(f"HELLO {name}!!!")


cli.add_command(generate_data)
cli.add_command(hello)

if __name__ == "__main__":
    cli()
