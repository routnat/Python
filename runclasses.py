'''
Created on 28 Dec 2019

@author: Nathan
'''
from airtravel import *
from pprint import pprint as pp

if __name__ == '__main__':
    f= Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    
    f.allocate_seat('12A', 'Dave')
    #f.allocate_seat('12A', 'Bill')
    f.allocate_seat('15F', 'Barry')
    f.allocate_seat('15E', 'Jane')
    #f.allocate_seat('E27', 'Joe')
    f.allocate_seat('1C', 'Lucy')
    f.allocate_seat('1D', 'Jack')
    #f.allocate_seat('DD', 'Bob')
    
    #pp(f._seating)
    
    f.relocate_passenger('12A', '15D')
    
    #pp(f._seating)
    
    print(f.num_available_seats())
    
    f.make_bording_cards(console_card_printer)