


t=float(input("请输入身高(米):"))
s=float(input("请输入体重(公斤):"))
BMI=s/t**2
if BMI < 18.5 :
    print(BMI,"体重过轻")
elif  18.5 <= BMI < 24 :
    print(BMI,"正常范围")
elif  BMI > 24 :
    print(BMI,"体重过重") 
