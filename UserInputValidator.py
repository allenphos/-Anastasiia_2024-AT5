class UserInputValidator:

    def validate_positive_integers(self, str_list):
        
        val_integers = []
        for item in str_list:
            if item.isdigit() and int(item) > 0:
                val_integers.append(int(item))
        return val_integers


    def display_message (self, val_list):
        val_integers = self.validate_positive_integers(val_list)
        if val_integers:
            print(f"List is validated. {len(val_integers)} valid positive integers found: {val_integers}")
        else:
            print("List is not validated. No valid positive integers found.")
            

