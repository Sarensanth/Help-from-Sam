def help_from_sam(a):
    count=1
    num=1
    while num*2<=a:
        num*=2
    return count+(a-num)

a=int(input())
print(help_from_sam(a))