from tkinter import *
from tkinter import filedialog
from pytube import Playlist
import webbrowser

# Url input And Printing Processes

url_input=input("Put Your URL Here : ")
print("\n")
process_list=["Open", "Download"]
print("--------------------------------------------------------------------")
list_enum=1
for i in process_list:
    print(f"{list_enum} : {i}")
    list_enum=list_enum+1
print("--------------------------------------------------------------------")
print("\n")

# Choices

process_input=int(input("Choose Process To Complete : "))

# open in browser

if process_input == 1:
    webbrowser.open(url_input)

# Download Functions

elif process_input == 2:
    print("\n")
    print("""

----------------------------------------------------------
          All Videos Inside Current Playlist
----------------------------------------------------------

    """)
    all_videos=Playlist(url_input).videos

  # Print All Videos Titles
    print("-------------------------------------------------------")
    video_enum=1
    for i in all_videos:
        print(f"{video_enum} : {i.title}")
        video_enum=video_enum+1
    print("-------------------------------------------------------")
    print("\n")

    # Confirmation inputing

    conf_input=input("Yes To Continue And No To Exit : ")
    print("\n")
    if conf_input.lower().startswith("y"):
        print("""

-----------------------------------------------------        
        Please Choose Directory To Save Files
-----------------------------------------------------
        
        """)
        forlder_name = filedialog.askdirectory()


        # Printing Title And Streams OF Current Video


        for i in all_videos:
            print(str(f"The current video Name is : {i.title}"))

            print("""

------------------------------------------------------------            
            Current Video Available Streams
------------------------------------------------------------

            """)
            stm_enum=0
            for n in i.streams:
                print(f"{stm_enum} : {n}")
                stm_enum=stm_enum+1

            # Choosing Stream And Download The Choice
            print("\n----------------------------------------------------------")
            stm_input=int(input("          Please Choose Suitable Stream : "))
            print("----------------------------------------------------------\n")

            video=i.streams[stm_input]
            video.download(forlder_name)
            print("""
            
-----------------------------------------------------            
            Video Downloaded Successfully
-----------------------------------------------------

            """)


        print("""

-----------------------------------------------------            
            Playlist Downloaded Successfully
-----------------------------------------------------

            """)

    # Cancellation Functions

    elif conf_input.lower().startswith("n"):
        print("OK, Good bye")
        exit()
    else:
        print("Write A correct Answer :(")
        exit()

else:
    print("\nChoose Right Choice :(")
    exit()
