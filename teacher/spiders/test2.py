
import re
if __name__ == '__main__':
    name='2017年中科院广州地化所各专业导师信息'
    p1 = re.compile(r'[0-9]+年')
    m=p1.search(name)

    name = re.sub(p1, ' ', name)
    # print(m.group())
    # print(name)
    print(len("交通与物流工程学院"))
