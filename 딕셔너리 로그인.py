user_info = { 'id' : 'software' , 'pw' : 'python'}
a = input()
b = input()

if(user_info['id'] != a and user_info['pw']==b):
    print("ID Mismatch!")
elif(user_info['id'] == a and user_info['pw']!=b):
    print("PW Mismatch!")
elif(user_info['id'] == a and user_info['pw']==b):
    print("Success in Login")
