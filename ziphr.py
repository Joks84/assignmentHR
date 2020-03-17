#postavka je dobra

plane_id = int(input("What is plane id? "))
pass_no = int(input("What is the number of passangers? "))
capacity = plane_id * 200
pass_con = pass_no * 0.002
fuel_con_min = plane_id * 0.80 + pass_con
flight_time = capacity / fuel_con_min

# required_fuel - potential question

print(plane_id)
print(pass_no)
print(capacity)
print(pass_con)
print(fuel_con_min)
print(flight_time)
