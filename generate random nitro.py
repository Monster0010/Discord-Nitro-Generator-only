import random
import string

def generate_random_text(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_nitro_links(num_links, length):
    base_url = "https://promos.discord.gg/"
    
    with open("output.txt", "w") as f:
        for _ in range(num_links):
            nitro_code = generate_random_text(length)
            nitro_link = base_url + nitro_code + "\n"
            f.write(nitro_link)

# Example usage
num_nitros = int(input("Enter the number of Nitro links to generate: "))
nitro_length = 25  # Length of each Nitro link

generate_nitro_links(num_nitros, nitro_length)