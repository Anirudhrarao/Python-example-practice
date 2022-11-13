name_marks = ['Anirudhra','A+',99,'Yash','A',98]
res = []
key_ls = ['Name','Grade','Marks']
for ind in range(0,len(name_marks),3):
    res.append({key_ls[0]:name_marks[ind],key_ls[1]:name_marks[ind+1],key_ls[2]:name_marks[ind+2]})
for item in res:
    print(item)
