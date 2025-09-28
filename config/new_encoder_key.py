from cryptography.fernet import Fernet

# при надобности заменить ключ в .env

if __name__ == '__main__':
    key = Fernet.generate_key()
    print(key)