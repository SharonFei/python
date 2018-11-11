try:
    aa="异常测试："
    print(aa)
except Exception as msg:
    print(msg)
finally:
    print("不管是否异常，我都会被执行！")
