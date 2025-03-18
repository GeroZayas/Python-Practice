import click
import faker
import rich


# from trogon import tui


# @tui()
@click.command("generate-data")
@click.option("-n", "--names", default=0, help="Number of fake names.")
@click.option("-w", "--words", default=0, help="Number of random words.")
@click.option("-e", "--emails", default=0, help="Number of fake email addresses.")
def generate_data(names, words, emails):
    "Generates fake names, random words, and fake email addresses."
    fake = faker.Faker()
    if names:
        fake_names = [fake.name() for _ in range(int(names))]
        click.echo("Fake Names:")
        click.echo("\n".join(fake_names))
    if words:
        fake_words = [fake.word() for _ in range(int(words))]
        click.echo("\nRandom Words:")
        click.echo("\n".join(fake_words))
    if emails:
        fake_emails = [fake.email() for _ in range(int(emails))]
        click.echo("\nFake Email Addresses:")
        click.echo("\n".join(fake_emails))


@click.command("hello-name")
@click.option("-t", "--name", default=0, help="Name")
def say_hello(name):
    "Says hello to NAME"
    click.echo(f"Hello {name}")


if __name__ == "__main__":
    generate_data()
    say_hello()
