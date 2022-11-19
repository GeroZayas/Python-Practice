# download YouTube mp3.py
# importing packages
from pytube import YouTube
import os
from rich import print


def repeat_process() -> bool:
    user_answer = input("Do you want to download another song 'y' or 'n': ")
    return True if user_answer == "y" or user_answer == '' else False


run = True

while run:
    # url input from user
    print("[bold blue]Enter the URL of the video you want to download:[/bold "
          "blue]")
    yt = YouTube(str(input("\n>> ")))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print(
        "[bold yellow]Enter the destination (leave blank for "
        "...'\\Downloads\\Pelis y Music'[/bold yellow]) "
    )
    destination = str(
        input(">> ")) or r"C:\Users\Gero Zayas\Downloads\Pelis y Music"

    # download the file
    out_file = video.download(output_path=destination)

    try:
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print(
            "-> "
            + yt.title
            + " <- [bold green]has been successfully downloaded.[/bold green]"
        )

        if repeat_process() == True:
            continue
        else:
            print("[bold lightblue]BYE BYE![/bold lightblue]")
            break

    except Exception:
        print("File Already Exists")
        print("[bold red]Not Downloaded[/bold red]")
    # result of success
