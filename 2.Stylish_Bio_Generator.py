import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion: ").strip()
emoji = input("Enter your emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple Lines ")
print("2. Vertical Flair ")
print("3. Emoji Sandwich ")

style=input("Enter your choice: ").strip()

def generate_bio(name, profession, passion, emoji, website, style):
    if style == "1":
        return f"{name} | {profession} | Passionate about {passion} {emoji}\nWebsite: {website}"
    elif style == "2":
        return f"{name}\n{profession}\nPassionate about {passion} {emoji}\nWebsite: {website}"
    elif style == "3":
        return f"{emoji*3} {name} - {profession} - Passionate about {passion} {emoji*3}\nWebsite: {website}"
    else:
        return "Invalid style choice."
    
bio = generate_bio(name,profession,passion,emoji,website,style)
print("\nYour Stylish Bio:")
print("*"*80)
print(textwrap.dedent(bio))
print("*"*80)

save = input("Do you want to save this bio to a file?(y/n)").lower().strip()
if save == 'y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(bio)
    print("Bio saved to", filename)