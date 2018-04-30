
import re
name='2017年中科院广州地化所各专业导师信息'
p1 = re.compile(r'[0-9]+年')
m=p1.search(name)

name = re.sub(p1, ' ', name)
# print(m.group())
# print(name)
