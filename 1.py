while True:
    try:
        days=range(1,32)
        months=range(1,13)
        years=range(1901,2020)
        d,m,y=int(input('day(1-31):')),int(input('Month(1-12):')),int(input('Year(1901-2020):'))
    except ValueError:
        print('Only integer numbers!')
        continue
    if (m%2==0 and d>=31 or m==2 and d>=28 and y%4!=0) and m!=12:
        d=1
        m+=1
    elif d<32:
        if m==2 and d<=27:
            d+=1
        elif m!=2:
            d+=1
    elif d>=32 and m==12:
        y+=1
        d=1
        m=1
    if y%4==0:
        if m==2 and d==28:
            d+=1
    print(f'Next day - Day:{d} Month:{m},Year:{y}')
    s=input('Rerun proggram?\nif yes press: 1\nelse press anything\n')
    if s=='1':
        continue
    else:
        break
    
