# Task - 1
print("Task # 1...")
name = "Muhammad Noman"
age = 21
sem = "5th"
edu_Level = "Under Graduate"
gen_Abilities = "I am a \"Footballl player\""

data = """My name is {} ,
and I am {} years old.
I am in {} semester {}.
{}."""
result = data.format(name,age,sem,edu_Level,gen_Abilities)
print(result)

# Task - 2
print("Task # 2 ...")
for x in name:
    print(x)
print("Reversed String...")
new = reversed(name)
for x in new:

    print(x)


