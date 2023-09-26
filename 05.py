cur_index = -1
prev_index = 0   
next_index = 0
my_list = []
while True:
        arr_input = input("Your Input : ")
        if arr_input == "prev" :
            prev_index = cur_index - 1
            if prev_index >= 0:
                cur_index = cur_index - 1 
            else:
                print("No website to previous")
        elif arr_input == "next" :
            next_index = cur_index + 1
            if next_index < len(my_list):
                cur_index = cur_index + 1 
            else:
                print("No website to go")
        elif arr_input == "current" :
            current_element = my_list[cur_index] 
            print("Now you on ",current_element)
        elif arr_input.startswith("input ") :
            ls = arr_input.split(" ")
            cur_index = cur_index + 1
            my_list.insert(cur_index, ls[1])
            if(cur_index < len(my_list)-1) :
                my_list.pop(cur_index+1)
        elif arr_input == "all" :
            print(my_list)