import mod_paid_process

# For n people, to calculate the value paid, used stratum validation and economic boost validation
# Para n personas, calcular el valor abonado, usando la validando el estrato y el impulso

n = mod_paid_process.int_validation("How many people do you want to add:")

total_value_n = 0

for i in range(0,n):
    name = input(f"\n{i+1} Enter a name:\n")
    stratum = mod_paid_process.stratum_validation(name)
    economic_boost = mod_paid_process.int_validation(f"Enter the economic boost of {name}:")
    amount_paid = mod_paid_process.paid_process(stratum, economic_boost)
    total_value_n += amount_paid
    print(f"\nThe amount paid for {name} is {amount_paid}")
print(f"\nThe total value is {total_value_n}\n")

# Vocabulary:
# economic_boost = impulso_economico
# value paid = valor abonado