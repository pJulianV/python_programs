def stop_validator(label, lst_nums):
    while True:
        try:
            dato = input(label)
            if dato.upper() == "STOP":
                return "STOP"
            lst_nums.append(int(dato))
        except ValueError:
            print("Error")
    return dato


nums = []
stop_validator("Enter nums (type \"STOP\" to stop)", nums)


min = nums[0]
max = nums[0]
for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]

    elif nums[i] < min:
        min = nums[i]
print(min, max)
