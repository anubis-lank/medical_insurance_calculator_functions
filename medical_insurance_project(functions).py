# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker

  output_message = "The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars."

  return output_message, estimated_cost 

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28, 0, 26.2, 3, 0)
print(maria_insurance_cost[0])


# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35, 1, 22.2, 0, 1)
print(omar_insurance_cost[0])

# Create a function to calculate the difference between the insurance costs (given as inputs) of any two individuals
def calculate_cost_difference(person1, person2):
  cost_diff = (person1 - person2) * -1

  print("The difference in insurance cost is "+str(cost_diff)+" dollars.")

calculate_cost_difference(maria_insurance_cost[1], omar_insurance_cost[1])