filename = input("filename: ")

new_filename = filename.lower().strip()

if '.gif' in new_filename:
    print("image/gif")
elif '.png' in new_filename:
    print("image/gif")
elif '.jpg' in new_filename:
    print("image/gif")
elif '.jpeg' in new_filename:
    print("image/gif")

elif '.pdf' in new_filename:
    print("application/pdf")
elif '.zip' in new_filename:
    print("application/zip")

elif '.txt' in new_filename:
    print("text/plain")

else:
    print("application/octet-stream")