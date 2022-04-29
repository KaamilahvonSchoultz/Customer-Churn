
import random
import string

def generate_id():
    alphabet = list(string.ascii_uppercase)
    id_numbers = [str(random.randint(0,9)) for _ in range(4)]
    id_letters = [random.choice(alphabet) for _ in range(5)]
    new_customer_id = f"{''.join(id_numbers)}-{''.join(id_letters)}"
    
    return new_customer_id
