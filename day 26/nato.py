import pandas
data=pandas.read_csv("C:/Users/ASUS/Downloads/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
data_frame=pandas.DataFrame(data)
new_dict={row.letter:row.code for (index,row) in data_frame.iterrows()}
try:
    user=input("ENTER THE WORD ").upper()
    for i in user:
        r=new_dict[i]
except KeyError:
    print("please type alphabet only!")
else:
    l=[n for n in user]
    result=[new_dict[i] for i in l if i in new_dict]
    # print(l)
    print(result)