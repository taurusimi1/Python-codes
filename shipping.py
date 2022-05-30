weight = 41.5
flat_charge= 20.00
premium_shipping = 125.00
# Ground Shipping
if weight <= 2.0:
  ground_cost = 20.00 + (1.50*weight)
  print("Ground Shipping:" + str(ground_cost))
  drone_cost = 4.50*weight
  print("Drone Shipping:" + str(drone_cost))
elif (weight >= 2.0) and (weight<=6.0):
  ground_cost = 20.00 + (3.00*weight)
  print("Ground Shipping:" + str(ground_cost))
  drone_cost = 9.00*weight
  print("Drone Shipping:" + str(drone_cost))
elif (weight >6.0) and (weight<=10.0):
  ground_cost = 20.00 + (4.00*weight)
  print("Ground Shipping:" + str(ground_cost))
  drone_cost = 12.00*weight
  print("Drone Shipping:" + str(drone_cost))
else:
 ground_cost = 20.00 + (4.75*weight)
 print("Ground Shipping:" + str(ground_cost))
 drone_cost = 14.25*weight
 print("Drone Shipping:" + str(drone_cost))
print("The cost of premium shipping is:" + str(premium_shipping))
if (ground_cost<premium_shipping) and (ground_cost<drone_cost):
  print("Ground Shipping is the cheapest")
elif (drone_cost<premium_shipping )and (drone_cost<ground_cost):
  print("Drone shipping is the cheapest")
else:
  print("Premium shipping is the cheepest")
