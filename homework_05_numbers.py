# ticket price
amount_of_people = 4
ticket = 500
total_ticket_cost = ticket * amount_of_people

# Taxi fare to and from the park
taxi_cost_to_park = 600
taxi_cost_from_park = taxi_cost_to_park * 1.2

# Discounted pizza price
pizza_cost = 250
discount_rate = 0.15
total_pizza_cost = (pizza_cost * 2) * (1 - discount_rate)

# air hockey
air_hockey_cost_per_game = 80
total_air_hockey_cost = air_hockey_cost_per_game * 8

# total cost
total_cost = (total_ticket_cost + taxi_cost_to_park + taxi_cost_from_park +
              total_pizza_cost + total_air_hockey_cost)

# each person cost
each_person_cost = total_cost / 4

print(f'{each_person_cost=}')
