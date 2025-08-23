import datetime

name = input("What is your name? ").strip()
age = input("What is your age? ").strip()
city = input("What is your city? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favourite hobby? ").strip()

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and in my free time, I enjoy {hobby}. "
    f"\nNice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\nLogged on: {current_date}"

border = "*"*80
final_output = f"{border}\n{intro_message}\n{border}"
print(final_output)