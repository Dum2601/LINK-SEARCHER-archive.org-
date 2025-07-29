from URL_operations.get_page import Page

def main(page_link):
    page = Page(page_link).download_link()

    if page:
        for link in page:
            print(link)
    else:
        print("No link found or error in page acess!")


def return_main_menu(leave_choice):
    if leave_choice.lower() == 'y':
        print("Ok... Farewell!")
        return False  # Indica saída do programa
    elif leave_choice.lower() == 'n':
        print('OK! Returning to Main Menu.')
        return True   # Retorna ao menu
    else:
        print("Unable to proceed: Choose Y or N next time.")
        return True    # Retorna ao menu por padrão


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
            main(archive_link)
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
