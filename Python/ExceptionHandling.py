try:
    f=open('sample1.txt','r')
except FileNotFoundError:
    print('File not found')
except NameError:
    print('variable not defined')
except ZeroDivisionError:
    print('Cant divide by zero')
except Exception as e:
    print(e)
else:
    print(f.read())
finally:
    print('ye to print hoga hi')