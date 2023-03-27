def make_album(name, title, num_tracks=""):
    """descibe a music album"""
    if num_tracks:
        album = {"Artist name": name, "Album title": title,\
                  "Number of Tracks": num_tracks}
    else:
        album = {"Artist name": name, "Album title": title}
    return album
print(make_album("Taylor Swift", "Folkore"))
print(make_album("Taylor Swift", "Red", 30))

while True:
    print("\nEnter album information: ")
    print("(enter 'q' at any time to quit)")
    a_name = input("Artist name: ")
    if a_name == "q":
        break
    a_title = input("Album Title: ")
    if a_title == "q":
        break
    n_tracks = input("Number of Tracks: ")
    if n_tracks == "q":
        break
    info = make_album(a_name, a_title, n_tracks)
    print("Your album is: \n", info)
