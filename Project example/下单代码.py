import pandas as pd
import numpy as np
import os
import warnings

'''
读取文件
'''

print("请输入源文件路径: ")

path = input()

df1 = pd.read_excel(path+'\下单表格.xIsx' )#将中文改成下单表格的名字

df2 = pd.read_excel(path+'\MB库存.xIsx')#将中文改成MB库存的名字

df3 = pd.read_excel(path+'\CZ多余表格.xIsx’)#将中文改成CZ多余表格的名字

df4 = pd.read_excel(path+'\OI多余表格.xIsx’)#将中文改成OI多余表格的名字

df3['物料代码'] = df3['物料编码']#列表头改名字,统一成物料代码

df3['CZ多余PR'] = df3['多余PR']#列表头改名字,区分不同组织数据

df3['CZ多余订单'] = df3['多余订单']

df3['CZ多余库存'] = df3['多余库存']

df4['物料代码'] = df4['物料编码']#列表头改名字,统一成物料代码

df4['OI多余PR'] = df4['多余PR']#列表头改名字,区分不同组织数据

df4['OI多余订单'] = df4['多余订单']

df4['OI多余库存'] = df4['多余库存']

df_all = pd.merge(df1[['物料代码','说明','供应商代码','协议号','建议订购日期','需求日期','可转数量','到期数量','执行数量']],df2,df3,df4,on=物料代码,how = 'left')

df_all['MB计划单'] = df.eval('MB计划单=计划单 + 预测计划单',inplace=True)#两列数据加和

df_al['差异'] = df.eval('差异=执行数量 - MB计划单',inplace=True)#两列数据相减

df_al['P0'] = df_all['在订']#从其他表格引数据

df_all['PR'] = df_all['未下单']#从其他表格引数据

df_all['CZ多余'] = df_all['CZ多余库存']#从其他表格引数据

df_all['CZ多余PO&PR'] = df.eval('CZ多余PO&PR = CZ多余PR + CZ多余订单',inplace=True)#两列相加

df_al['OI多余'] = df_al['多余库存']#从其他表格引数据

df_all['OI多余PO&PR'] = df.eval('OI多余PO&PR = OI多余叙PR + OI多余订单',inplace=True)#两列相加.

df_all = df_al[['物料代码','说明','供应商代码','协议号','建议订购日','需俅日期','可转数量','到期数量','执行数量','MB计划单','差异','PO','PR','CZ多余','CZ多余PO&PR','OI多余','OI多余PO&PR']]

print('请输入输出文件路径:')
path2 = input()

df_all.to_excel(path+'\MB组织下单xlsx',index =False)#中文可改成MB组织下单