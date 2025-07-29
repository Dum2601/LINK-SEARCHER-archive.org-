import subprocess
import os
from datetime import datetime
from URL_operations.get_page import Page

def main(page_link):
    page = Page(page_link).download_link()
    if page:
        index = 0
        link_arr = []
        for link in page:
            print(f'{index}: {link}')
            index += 1
            link_arr.append(link)
        return link_arr
    else:
        print("No link found or error accessing the page!")

def return_main_menu(leave_choice):
    if leave_choice.lower() == 'y':
        print("Ok... Farewell!")
        return False
    elif leave_choice.lower() == 'n':
        print('OK! Returning to Main Menu.')
        return True
    else:
        print("Unable to proceed: Choose Y or N next time.")
        return True

def menu():
    while True:
        print("\n========================= LINK SEARCHER =========================")
        print("================= Use Your Keyboard To Navigate =================")
        print("1. Option 1 - Search Download Links in Desired Page?")
        print("2. Option 2 - Info")
        print("3. Option 3 - Quit")
        choose = input("Choose an option: (1-3): ")

        if choose == '1':
            archive_link = input("Paste an archive.org item page link here to search links to download: ")
            links = main(archive_link)
            if not links:
                continue
            arr_size = len(links) - 1
            print(f"Choose an option between 0 and {arr_size}")
            which_download = input("Which link should I download? ")
            if which_download.isdigit():
                index = int(which_download)
                if 0 <= index <= arr_size:
                    chosen_link = links[index]
                    file_name = chosen_link.split("/")[-1]
                    print(f"Downloading: {file_name} ...")
                    subprocess.run(['curl', '-L', '-o', file_name, chosen_link])
                    print(f"\nDownload completed: {file_name}")
                    print(f"File saved in: {os.getcwd()}")
                    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                else:
                    print("Invalid option!")
            else:
                print("Please enter a valid number!")
            leave_choice = input('Do you really want to leave now? Confirm: (Y/n): ')
            if not return_main_menu(leave_choice):
                break
        elif choose == '2':
            print("With this algorithm, you can easily search download links on the desired page.")
            leave_choice = input('Press any key to return to menu: ')
            if leave_choice:
                continue
        elif choose == '3':
            leave_choice = input('Do you really want to leave? Confirm: (Y/n): ')
            if not return_main_menu(leave_choice):
                break
        else:
            print("Unable to proceed: Choose a number between 1 and 3.")
