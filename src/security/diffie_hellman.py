def calculate_key(shared_base, shared_prime, secret_key):
    return (int(shared_base) ** int(secret_key)) % int(shared_prime)
