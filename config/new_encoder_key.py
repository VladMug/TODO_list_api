from cryptography.fernet import Fernet

# If necessary, replace the key in .env

if __name__ == '__main__':
    key = Fernet.generate_key()
    print(key)