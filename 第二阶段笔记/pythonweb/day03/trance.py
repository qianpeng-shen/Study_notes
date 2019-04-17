# a=10
# try:
#     b=a/'1'
# except TypeError as e:
#     print(e)
# print("++++++++++++++++")
import traceback
a=10
try:
    b=a/'1'
except TypeError as e:
    traceback.print_exc()
print("+++++++++++++++++++")