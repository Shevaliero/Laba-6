while True:
    try:
        days=range(1,32)
        months=range(1,13)
        years=range(1901,2020)
        d,m,y=int(input('day(1-31):')),int(input('Month(1-12):')),int(input('Year(1901-2020):'))
    except ValueError:
        print('Only integer numbers!')
        continue
    d1,m1,y1=d,m,y
    d2,m2,y2=d,m,y
    if m==2 and d>29 and y%4!=0:
        print('Max 28 days in this month!')
        continue
    if m==2 and d>29 and y%4==0:
        print('Max 29 days in this month!')
        continue
    if d>31 or d<1 or m>12 or m<1 or y>2020 or y<1901:
        print('Wrong range')
        continue
    if (m%2==0 and d>=31 or m==2 and d>=28 and y%4!=0) and m!=12:
        d1=1
        m1+=1
    elif d<32:
        if m==2 and d<=27:
            d1+=1
        elif m!=2 and m!=12:
            d1+=1
    if d>=31 and m==12:
        y1+=1
        d1=1
        m1=1
    if y%4==0:
        if m==2 and d==28:
            d1+=1
    if d==1:                        #Previous day
        if m!=3 and m!=1:
            d2-=1
        elif m==3:
            if y%4==0:
                d2=29
            elif y%4!=0:
                d2=28
        elif m==1:
            d2=32
            m2=12
            y2-=1
    print(f'\nNext day - Day:{d1} Month:{m1} Year:{y1}')
    print(f'\nPrevious day - Day{d2} Month{m2} Year{y2}')
    s=input('\nRerun proggram?\nif yes press: 1\nelse press anything\n')
    if s=='1':
        continue
    else:
        break
    
