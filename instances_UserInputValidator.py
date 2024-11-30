from UserInputValidator import UserInputValidator  


validator_instance1 = UserInputValidator()
validator_instance2 = UserInputValidator()

list1 = ["apple", "0", "7", "9", "-974"]
list2 = ["-100", "dog", "40", "cat", "236"]

print("Results 1:")
valid_integers1 = validator_instance1.validate_positive_integers(list1)
validator_instance1.display_message(list1)

print("\nValidator 2 Results:")
valid_integers2 = validator_instance2.validate_positive_integers(list2)
validator_instance2.display_message(list2)
