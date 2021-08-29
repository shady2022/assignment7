dic=[]
        
        
def show_menu():
        print('1-add new word')
        print('2-trans en2per')
        print('3-trans per2en')
        print('4-exit')
        
myfile = open('database.txt', 'r')

def add():
    eng = input('please write eng word:')
    per = input('please write per word:')
    
    dic.append({'eng': eng, 'per': per})
    dic.list=dic.split('\n')
    print(dic.list) 
    print('add new vocab succefully..')
    
def trans_en2per():
    sentence=input('please write your sentence:')
    data=sentence.split( )
    for i in range(len(dic)):
        for j in range(len(data)):
            if data[i]== dic[j]['persian']:
                print(dic[j]["wordper"], end=" ")
                break
            
                
def trans_per2en():
    sentece = input("please write your sentence: ")
    data1 = sentece.split( )
    for i in range(len(dic)):
        for j in range(len(data1)):
            if data1[i]== dic[j]["english"]:
                print(dic[j]["wordeng"], end=" ")
                break

show_menu()                       
while True:
    choice = input("What should we do? Select from the list.")
    if choice=="1":
        add()
    elif choice=="2":
        trans_en2per()
    elif choice=="3":
        trans_per2en()
    elif choice=="4":
         exit()              