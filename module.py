from tkinter import *
from tkinter import filedialog
from functools import partial
import time
import os

def empty_containers(**container):
    """
    this function will delete all of the items from a container
    when the container is a tuple then, it will yield an empty tuple
    otherwise it will delete every item from each passed container
    """
    new_tuple = ()
    for cont in container:
        if isinstance(container[cont], tuple):
            yield new_tuple
            continue
        container[cont].clear()
    return new_tuple


def list_dic(keys, values, token = None):
    """
    bind keys and values to make a dictionary
    this token is useful, when dealing with values of lists
    otherwise it return a dictonary
    """
    list_dic = dict()
    if token == 'ld':
        for key in keys:
            li = []
            for value in values:
                if key in value:
                    li.append(value)
            list_dic[key] = li
        return list_dic
    else:
        item_counter = 0
        for key in keys:
            list_dic[key] = values[item_counter]
            item_counter +=1
        return list_dic


def sorted_indices(old, new):
    """
    this function used to see the difference between the old non sorted list 
    with sorted list to know the new location of each file and each file's creation time 
    for dictionary binding
    """
    current_indices_values = []
    for j in old:
        for k in new:
            if j == k:
                current_indices_values.append(new.index(j))
    return current_indices_values        
       

def keys_values_tied_sorted(old_values, keys):
    """
    according to the returned value by sorted_indices
    the new sorted values(files) will be returned
    """
    new_index = sorted_indices(keys, sorted(keys))
    empty_string = ""
    organized_values = [empty_string for _ in range(0,len(keys))]
    counter = 0
    for k in new_index:
        organized_values[k] = old_values[counter]
        counter += 1
    return organized_values


def time_conversion(time_con):
    """time_con must be in ctime format
       converting it to tuple then to a specific format
    """
    if isinstance(time_con, time.struct_time):
        return time.strftime("%H:%M:%S %d %b %Y", time_con)
    else:
        tuple_time = time.strptime(time_con, "%a %b %d %H:%M:%S %Y")
        formated_time = time.strftime("%H:%M:%S %d %b %Y", tuple_time)
        return formated_time
    
def get_file_time_epoch(files, token=None):
    """
    return the creation time of each files with a specific format then convert it to seconds
    if token is 'o' then it returns sorted list
    otherise non sorted list
    """
    list_files_time = []
    for file in files:
        file_created_time = time.ctime(os.path.getctime(file))#the time in string format of the file 
        convert_each_ctime_new_format = time_conversion(file_created_time)#change the format of the file's time
        convert_each_ctime_new_format_tuple = time.strptime(convert_each_ctime_new_format, "%H:%M:%S %d %b %Y")
        list_files_time.append(time.mktime(convert_each_ctime_new_format_tuple))
    if token == 'o':
        return sorted(list_files_time)
    return list_files_time


