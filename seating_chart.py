import csv
from tabulate import tabulate
import re
import pandas as pd

class EditSeating:
    def __init__(self, selected_seating):
        self.selected_seating = selected_seating
    def validate(self):
        matches = re.search(r'^([A-E]{1})([1-8]{1})$', self.selected_seating)
        if not matches:
            return False
        elif matches:
            return True
    def return_groups(self):
        bruh = re.search(r'^([A-E]{1})([1-8]{1})$', self.selected_seating)
        if bruh:
            return bruh.group(1), bruh.group(2)

def main():

    seating = []
    get_data(seating)
    show_seating(seating)

    edit = EditSeating(selected_seating=get_request())
    if edit.validate() == True:
        print('ok') #placeholder
        book_seating(edit)
    elif edit.validate() == False:
        print('Unavailable, please try again')


def get_data(seating):
    with open('chart.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            seating.append(row)

def show_seating(seating):
    tab = tabulate(seating, headers='keys', tablefmt='fancy_grid')
    print(tab)

def get_request():
    request = input('which seat would you like to book?:').strip().upper()
    return request
def book_seating(edit):
    row, column = edit.return_groups()
    df = pd.read_csv('chart.csv', index_col=0)
    confirm = input('confirm?Y/N:').strip().upper()
    if confirm == 'Y':
        if df.loc[row, column] == 'X':
            print('This seat is taken.')
            return
        else:
            df.loc[row, column] = 'X'
            df.to_csv('chart.csv')
            view = input('view?Y/N:').strip().upper()
            if view == 'Y':
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            else:
                print('canceled')
    else:
        print('cancelled')




if __name__ == '__main__':
    main()
