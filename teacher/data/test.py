test="""
李勃 深圳研究院（能源与环境学部）
赵乾 机械工程学院
张辉 机械工程学院,工程物理系
褚祥诚 材料学院
王睿 水利水电工程系
陈宇 理学院
王强 土木工程系
崔爱莉 理学院
李琦 深圳研究院（信息与技术学部）
方菲 航天航空学院
朱永法 理学院 
阎培渝 土木工程系
孟永钢 机械工程学院
李鑫 机械工程学院
邵天敏 机械工程学院
张涛 信息科学技术学院
赵世玺 深圳研究院（能源与环境学部）
李宝华 深圳研究院（能源与环境学部）
成波 机械工程学院
张毅 信息科学技术学院
刘莉 机械工程学院
郑泉水 航天航空学院
李勃 深圳研究院（能源与环境学部）
王进 深圳研究院（能源与环境学部）
赵乾 机械工程学院
王睿 水利水电工程系
向东 机械工程学院
黎维彬 深圳研究院（能源与环境学部） 
张宝清 化学工程系
李博 航天航空学院
"""
save=[t.split(' ')[0] for t in test.split('\n') if len(t)>0]
print(','.join(set(save)))