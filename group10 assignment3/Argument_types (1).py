def student_info(name, age):
    print(f"my name is {name} and age is {age} years old")

# Positional argument
student_info('dorrie', 20)

# Keyword argument
student_info(age=21, name="dorrie")


# Default argument
def student_info(name='gift', age=18):
    print(f"my name is {name} and age is{age} years old")

student_info()
student_info("marry", 20)


# *args and **kwargs
def student_info(name, age=18, *args, **kwargs):
    print(f"my name is{name} and age is {age} years old")
    print("args:", args)
    print("kwargs:", kwargs)

student_info(
    "dorrie",
    22,
    "Computer Science", "Year 2",
    university="Ardhi University",
    GPA=3.5
)

# *args and **kwargs

