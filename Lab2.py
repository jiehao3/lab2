def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")     

def get_user_input():
    x = input()
    y = x.split(",")
    z = [float(num) for num in y]
    return z
    
def calc_average(temperatures):
   return (sum(temperatures) / len(temperatures))

def calc_min_max_temperature(temperatures):
    return [min(temperatures), max(temperatures)]

def sort_temperature(temperatures):
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    x = sorted(temperatures)
    y = len(temperatures)
    if y%2==0:
        a = int(y/2)
        b = int(y/2)+ 1
        median_temperature = [x[a], x[b]]
    else:
        median_temperature = x[y//2]
    return median_temperature

display_main_menu()
temperatures = get_user_input()
print(calc_average(temperatures))
print (calc_min_max_temperature(temperatures))
print (sort_temperature(temperatures))
print (calc_median_temperature(temperatures))