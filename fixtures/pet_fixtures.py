pet_name_valid = ["doggy", "123doggy", "123", "!@#$%^&*()_+=-", "dog" * 500]
pet_name_invalid = ["", " ", "dog" * 50000, 123]
pet_edit_status = ["available", "pending", "sold"]
pet_edit_status_invalid = ["not_exist_status", 123, True, "", "   "]
