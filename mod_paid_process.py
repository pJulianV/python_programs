
# * module with the functions of paid process

# ! Vocabulary:
# ? paid process = proceso abonado
# ? impulses_consumption = cosumo de impulsos

def paid_process(stratum, economic_boost):
    if stratum == 1:
        basic_rate = 10000
    elif stratum == 2:
        basic_rate = 15000
    elif stratum == 3: 
        basic_rate = 20000
    elif stratum == 4:
        basic_rate = 25000
    elif stratum == 5:
        basic_rate = 30000
    economic_boost_consumption = 100 * economic_boost
    return economic_boost_consumption + basic_rate

def int_validation(input_txt):
    while True:
        try:
            int_data = int(input(f"\n{input_txt}\n"))
            break
        except ValueError:
            print("\n| Enter a integer value |")
    return int_data


def stratum_validation(name):
    while True:
        try:
            stratum = int(input(f"\nEnter the {name} stratum (1-5):\n"))
            if stratum >= 1 and stratum <= 5:
                break
            else:
                print("\nEnter a value between 1 and 5")
        except ValueError:
            print("\n| Enter a integer value |")
    return stratum

# ! print(paid_process(int(input()), int(input()))) 