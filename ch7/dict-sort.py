# 기장5
# 송정 23
# 세미나 10
# 체대 2
# 황령산 3
# 감천 1

import operator

trainDic,trainlist = {},[]

trainDic = {'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든','James':'제임스'}
trainlist = sorted(trainDic.items())
print('키로 오름차순' , trainlist)
trainlist = sorted(trainDic.items(),reverse=True)
print('키로 내림차순',trainlist)
trainlist = sorted(trainDic.items(),key=operator.itemgetter(1))
print('값으로 내림차순',trainlist)
trainlist = sorted(trainDic.items(),key=operator.itemgetter(1),reverse=True)
print('값으로 내림차순',trainlist)