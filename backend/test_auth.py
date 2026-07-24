from app.auth import hash_password

hashed = hash_password("Password123")

print("Original Password:", "Password123")
print("Hashed Password:", hashed)