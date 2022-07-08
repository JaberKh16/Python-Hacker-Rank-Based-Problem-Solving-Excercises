if __name__=='__main__':
    ns_eng_sub = int(input())
    ns_eng_sub_list = []
    # english newspaper subscription students
    for ns_subs_eng in range(ns_eng_sub):
        ns_subs_eng = input()
        ns_eng_sub_list.append(ns_subs_eng)
    # print(ns_eng_sub_list)
    
    ns_frnch_sub = int(input())
    ns_frnch_sub_list = []
    # english newspaper subscription students
    for ns_subs_frnch in range(ns_frnch_sub):
        ns_subs_frnch = input()
        ns_frnch_sub_list.append(ns_subs_frnch)
    # print(ns_eng_sub_list)
    
    # making a set of english newspaper subscription students
    eng_subs_stu_set = set(ns_eng_sub_list)
    # print(eng_subs_stu_set) 
    # making a set of french newspaper subscription students
    frnch_subs_stu_set = set(ns_frnch_sub_list)
    # print(frnch_subs_stu_set)
    # finding the symmetric difference and print its length
    symmertic_diff = eng_subs_stu_set.symmetric_difference(frnch_subs_stu_set)
    print(len(symmertic_diff))
    
    

# solve-2
# making a set of english newspaper subscription students
eng_subs_stu_set = set(input().strip())
# print(eng_subs_stu_set) 
# making a set of french newspaper subscription students
frnch_subs_stu_set = set(input().strip())
# print(frnch_subs_stu_set)
# finding the symmetric difference and print its length
symmertic_diff = eng_subs_stu_set.symmetric_difference(frnch_subs_stu_set)
print(len(symmertic_diff)-1)