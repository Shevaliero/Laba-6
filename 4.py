while True:
    try:
        t = float(input('Input minutes(0-60):'))
    except ValueError:
        print('Only numbers!')
        continue
    if 0<=t<=60:
        while t>6:
            t -= 6
        if 0<=t<3 or t==6:
            print('Green')
        elif 3<=t<4:
            print('Yellow')
        elif 4<=t<6:
            print('Red')
    s=input('Rerun proggram?\nIf yes press: 1\nElse press anything\n')
    if s=='1':
        continue
    else:
        break
