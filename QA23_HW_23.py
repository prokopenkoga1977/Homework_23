#1) Get user name 

# Expect : “jOhN”

# Result  : ”John” 

name="jOhN"
print(name.capitalize())

#2) Get user surname and split it by latter 

# DOE
# D O E 

surname = "DOE"
print(" ".join(surname))


# 3) Get user age and return year of birth 

user_age=input("Age: ")
import datetime 
year_of_birth=datetime.date.today().year-int(user_age)
print("Year of birth: ",year_of_birth)

# 4) Equal userAge and : 15 ; 23 ;13 and print it to the screen ;

# To every option use : <= , >= , < , > , ==

# int()

user_name=input("What is your name?: ")
user_surname=input("What is your surname?: ")
user_age=input("How old are you?: ")
if int (user_age)<13:
    print (user_name)
if int(user_age)  >=13 and int(user_age)<=23:
    print ("Teenager") 
if int(user_age)==23:
     print(user_name)
if int(user_age)>23:
    print(user_surname)    

# 5)
# Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil  laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima
# quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas
# eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis
# numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum!
# Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo
# alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure
# laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga
# quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error
# temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores
# quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum
# libero enim natus! Cum, corrupti ad.

# -Find “ad” position 
# -Slice “ad” from text
# -Replace all “Lorem” on “Hey you”
text ="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil  laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima
quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas
eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis
numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum!
Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo
alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure
laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga
quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error
temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores
quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum
libero enim natus! Cum, corrupti ad."""
print(text.find("ad"))
ad=text[text.find("ad"):]
print(ad)
txt=text.replace("Lorem", "Hey you")
print(txt)

# Until "STOP"

# data_bace =[]

# 1) Registration

# 2) Authorization 

# 4) if login length less than 5 characters print an Error

# 5) if password contains more than 10 symbols throw an Error 

# USE : split , slice , create other variables .
# Do everything that you want to , but remember that all data above must exist .

print("================================================================")
data_base=[]
is_running = True
is_valid = None

while is_running:
    user_email=input("Enter your email: ")
    user_name=input("Enter your name: ")
    user_password=input("Enter your password: ")

    def email_validation():
        global user_email
        if len(user_email)>=5:
            return True
        else:
            print("Error! Enter email more than 5 characters")

    def password_validation():
        global user_password
        if len(user_password)<=10:
            return True
        else:
            print("Error! Password must be less than 10 characters")
    def registration (user_email, user_name, user_password, data_base):
        global is_valid
        global is_running

        is_valid_email=email_validation()
        is_valid_password=password_validation()

        if is_valid_email and is_valid_password:
            is_valid = True
            data_base.append({
                "Name": user_name,
                "Email": user_email,
                "Password": user_password
            })
            is_valid = False

    registration(user_email, user_name, user_password, data_base)
    user_choose = int(input("1) Exit 2) Continue ")) 
    if user_choose == 1:
        is_running = False
print(data_base)

user_email = input("Enter your email: ")
user_password = input("Enter your password: ")

for user in data_base :
    for value in user.values() :
        if value == user_email: 
            print(f"Hello {user['Name']}!")
                    
            if user_password == user['Password']:
                print("Welcome!")
            else:
                print("Password is incorrect!")

