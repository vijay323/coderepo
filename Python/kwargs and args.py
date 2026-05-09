def  Pracrtice(**kwargs):
    for key,value in kwargs.items():
        print(f'key:{key} value={value}')


print(Pracrtice(Name='Vijay',age=23,stream='MCA'))