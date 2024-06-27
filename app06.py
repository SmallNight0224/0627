print('計算體積')
x=int(input('輸入長:'))
y=int(input('輸入寬:'))
c = x * y
print('體積是',c)
if 100>=c:
    print("這是小面積")
else:
    print("這是大面積")