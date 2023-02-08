import yagmail
yag = yagmail.SMTP('gerozayas@gmail.com', 'Clavegerozayas7')
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('gerozayas@gmail.com', 'subject', contents)