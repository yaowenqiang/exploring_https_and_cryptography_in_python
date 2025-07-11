from croptography.fernet import Fernet
ke = Fernet.generate_key()
my_cipyer = Fernet(key)
cipher_text = my_cipyer.encrypt('hello world')
