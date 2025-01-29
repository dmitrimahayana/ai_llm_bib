from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

if __name__ == '__main__':
    pass_str = input("Enter your password: ")
    new_pass = get_password_hash(pass_str)
    print(new_pass)