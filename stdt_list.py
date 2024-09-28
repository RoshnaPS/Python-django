def check_stdt(roll_no,stdt_list):
    if roll_no in stdt_list:
        print("student is present")
    else:
        print("student is absent")
stdt_list=[1,10,5,26,30,4]
roll_no=int(input("Enter the students roll no"))
check_stdt(roll_no,stdt_list)