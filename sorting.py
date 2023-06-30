from tkinter import *
from tkinter import messagebox
import random
import time

unsorted_data = data = []
select = ""

def draw_data(data, colors):
    
    canvas.delete("all")
    canvas_height = 500
    canvas_width = 800
    x_width = canvas_width / (len(data) + 1)
    offset = 20
    spacing = 10

    normalize_data = [i / max(data) for i in data]

    for i, rec_height in enumerate(normalize_data):
        x_initial = i * x_width + offset + spacing
        y_initial = canvas_height - rec_height * 460

        x_final = (i+1) * x_width + offset
        y_final = canvas_height

        canvas.create_rectangle(x_initial, y_initial,
                                x_final, y_final, fill=colors[i])
        canvas.create_text(x_initial + 2, y_initial,
                           anchor=SW, text=str(data[i]))

    main_prog.update_idletasks()

def generate_array():
    
    global data, unsorted_data

    min_val = int(min_value.get())
    size_val = int(size_value.get())
    max_val = int(max_value.get())

    if(min_val > max_val):
        messagebox.showwarning(
            message="Max. value should not be less than Min. value")
        min_val, max_val = max_val, min_val

    data = []

    for i in range(size_val):
        data.append(random.randrange(min_val, max_val + 1))

    unsorted_data = data.copy()
    draw_data(data, ["red" for x in range(len(data))])

def reset_array():
    global data
    data = unsorted_data.copy()
    draw_data(data, ["red" for x in range(len(data))])

def option_select(val):
    global select
    select = val

def bubble_sort(data):
    
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            draw_data(data, ["yellow" if x == j or x == j +
                      1 else "red" for x in range(len(data))])
            time.sleep(0.1)

def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])

        draw_data(array, ["yellow" if x == j or x == i or x == high
                    else "red" for x in range(len(array))])
        time.sleep(0.2)

 
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
    
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
        quickSort(array, pi + 1, high)

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            time.sleep(0.075)
            draw_data(arr,["yellow" if x == j or x == min_index else "red" 
                       for x in range(len(arr))])
            if arr[j] < arr[min_index]:
                min_index = j
        time.sleep(0.2)        
        draw_data(arr,["yellow" if x == i or x == min_index else "red" 
                       for x in range(len(arr))])
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
def insertionSort(arr):
     
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                time.sleep(0.2)        
                draw_data(arr,["yellow" if x == i or x == j else "red" 
                       for x in range(len(arr))])
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        swapped = False

        for i in range (start, end):
            if (a[i] > a[i+1]) :
                time.sleep(0.1)
                draw_data(a,["yellow" if x == i or x == i+1 else "red" 
                       for x in range(len(a))])
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True

        if (swapped==False):
            break

        swapped = False
        end = end-1
 
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                time.sleep(0.1)
                draw_data(a,["yellow" if x == i or x == i+1 else "red" 
                       for x in range(len(a))])
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start = start+1

def run_sort():
    
    global data, select
    size = len(data)
    print(select)
    if select == "Bubble Sort":
        bubble_sort(data)
    elif select == "Quick Sort":
        quickSort(data, 0 , size-1)
    elif select == "Selection Sort" or select == "":
        selection_sort(data)
    elif select == "Insertion Sort":
        insertionSort(data)
    elif select == "Cocktail Sort":
            cocktailSort(data)

    for i in range(size):
        time.sleep(0.05)
        draw_data(data, ["green" if x <= i else "red" for x in range(size) ])

main_prog = Tk()
main_prog.title("Sorting Algorithms Visualization")
main_prog.maxsize(800, 800)
main_prog.config(bg="grey")

UI_frame = Frame(main_prog, width=800, height=300, bg="grey")
UI_frame.grid(row=0, column=0)
Label(UI_frame, bg="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
Button(UI_frame, text="Start", command=run_sort,
       bg="green").grid(row=2, column=1, padx=5, pady=5)

size_value = Scale(UI_frame, from_=0, to=30, resolution=1,
                   orient=HORIZONTAL, label="Select Size", bg="ivory")
size_value.grid(row=1, column=0, padx=5, pady=5, sticky=W)

min_value = Scale(UI_frame, from_=0, to=100, resolution=10,
                  orient=HORIZONTAL, label="Select Min. value", bg="ivory")
min_value.grid(row=1, column=1, padx=5, pady=5, sticky=W)

max_value = Scale(UI_frame, from_=0, to=500, resolution=10,
                  orient=HORIZONTAL, label="Select Max. value", bg="ivory")
max_value.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=generate_array,
       bg="blue").grid(row=2, column=2, padx=5, pady=5)

Button(UI_frame, text="Reset", command=reset_array,
       bg="blue").grid(row=2, column=3, padx=5, pady=5)

options = ["Selection Sort", 
           "Bubble Sort", 
           "Quick Sort",
           "Insertion Sort",
           "Cocktail Sort"]

selected_options = StringVar(UI_frame)
selected_options.set(options[0])

OptionMenu(UI_frame, selected_options, *options, command = option_select ).grid(row=1, column=3, padx=5, pady=5)

canvas = Canvas(main_prog, width=800, height=500, bg="white")
canvas.grid(row=1, column=0)

main_prog.mainloop()
