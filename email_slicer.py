import re
def email_slicer():
    while True:
        email_info = input("Please enter your email: ")
        if not re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email_info):
            print("Please enter an valid email")
        else:
            break
    # slicing user name by using index to get index of '@'
    user_name = email_info[:email_info.index("@")] 
    #print(user_name)
    # slicing the domain name without '.com'
    domain_info = email_info[email_info.index('@')+1:email_info.index('.')].lower()
    #email_info.split('@')[1] is another method to slice domain name
    #print(domain_info)
    if domain_info == 'gmail':
        print(f"Hi {user_name}. I see your domain is registered with GOOGLE. That's cool !!!")
    elif domain_info == 'yahoo':
        print(f"Hi {user_name}. I see your domain is registered with YAHOO. That's cool !!!")
    elif domain_info == 'hotmail':
        print(f"Hi {user_name}. I see your domain is registered with HOTMAIL. That's cool !!!")
    else:
        print(f"Hi {user_name}.Looks like you have your own custom domain setup at {domain_info.upper()}. That's impressive !!!")
        
email_slicer()

