input_list = []
with open("input.txt","r") as f:
    input_list = f.readlines()

def organize_input_list():
    for i,line in enumerate(input_list):
        array = line.split(" ")
        limits = array[0].split("-")
        lower_limit = int(limits[0])
        upper_limit = int(limits[1])
        array[1] = array[1].strip(":")
        array[2] = array[2].strip("\n")
        array[0] = upper_limit
        array.insert(0, lower_limit)
        input_list[i] = array

def password_policy_one():

    correct_passwords = 0

    for line in input_list:
        lower_limit = line[0]
        upper_limit = line[1]
        letter = line[2]
        test_string = line[3]
        # print(f"{letter} {test_string} {test_string.count(letter)} {lower_limit} {upper_limit} {lower_limit <= test_string.count(letter) <= upper_limit}")
        if lower_limit <= test_string.count(letter) <= upper_limit:
            correct_passwords += 1
    return correct_passwords

def password_policy_two():

    correct_passwords = 0

    for line in input_list:
        first_index = line[0] - 1
        second_index = line[1] - 1
        letter = line[2]
        test_string = line[3]

        try:
            if (test_string[first_index] == letter and test_string[second_index] != letter) or (test_string[first_index] != letter and test_string[second_index] == letter):
                correct_passwords += 1
        except:
            pass

    return correct_passwords

organize_input_list()
#print(password_policy_one())
print(password_policy_two())