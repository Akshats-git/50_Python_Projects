def friendship_score(name1,name2):
    name1,name2 = name1.lower(),name2.lower()
    score=0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score+=len(shared_letters)*5
    score+=len(vowels & shared_letters)*10

    return min(score,100)

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

print("Friendship Compatibility Calculator")
print("Friendship Score: ",friendship_score(name1,name2))