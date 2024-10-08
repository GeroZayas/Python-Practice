import webview


def open_confirmation_dialog(window):
    result = window.create_confirmation_dialog(
        "Question", "Do you want to do it or what?"
    )
    if result:
        print("User clicked OK")
    else:
        print("User clicked Cancel")


if __name__ == "__main__":
    window = webview.create_window(
        "Confirmation dialog example", "https://www.gerozayas.com"
    )
    webview.start(open_confirmation_dialog, window)
