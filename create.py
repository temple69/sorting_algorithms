import os
files=['1-insertion_sort_list.c','100-shell_sort.c','1000-sort_deck.c','101-O','101-cocktail_sort_list.c','102-O','102-counting_sort.c','103-O','103-merge_sort.c','104-O','104-heap_sort.c','105-radix_sort.c','106-O','106-bitonic_sort.c','107-O','107-quick_sort_hoare.c','2-O','2-selection_sort.c','3-O','3-quick_sort.c','deck.h','print_array.c','print_list.c','sort.h']

def createfile(arr):
    for i in range(len(arr)):
       open(f'{os.getcwd()}/{arr[i]}','x')

createfile(files)  