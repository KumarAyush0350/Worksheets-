states = {"red": 4, "red_amber": 3, "green": 5, "amber": 3}


steps = int(input("Enter the numebr of steps:"))


current_state = "red"
print(f"Time {0:03d} State {current_state}")


time_in_state = 1


for t in range(1, steps + 1):
    
    if time_in_state == states[current_state]:
       
        if current_state == "red":
            current_state = "red_amber"
        elif current_state == "red_amber":
            current_state = "green"
        elif current_state == "green":
            current_state = "amber"
        elif current_state == "amber":
            current_state = "red"
        
     
        time_in_state = 0

    
    print(f"Time {t:03d} State {current_state}")
    
 
    time_in_state += 1