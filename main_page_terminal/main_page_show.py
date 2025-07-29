# MeuProjeto / MyProject
# Copyright (C) 2025 Douglas Barbosa
#
# Este programa é software livre: você pode redistribuí-lo e/ou modificá-lo
# sob os termos da Licença Pública Geral GNU publicada pela Free Software Foundation,
# na versão 3 da Licença, ou (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que seja útil,
# mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO.
# Consulte a Licença Pública Geral GNU para mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.



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
