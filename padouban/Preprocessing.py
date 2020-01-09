# coding=gbk
import pandas as pd
#查看数据
def start_read():
                # 读取csv格式的数据
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='utf-8',index_col=0)
                # 查看数据维度
                print(df.shape)
                # 查看数据信息
                print(df.info() )
                # 查看各列的名称
                print(df.columns )
                # 查看列的数据类型
                print(df['id'].dtype)

#去除重复值
def remove_duplicates():    #去除重复值
                # 读取csv格式的数据
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='utf-8',index_col=0)
                # 删除含有空值的行
                df.dropna(how='any')
                # 判断重复数据记录
                isDuplicated = df.duplicated()
                print(isDuplicated)
                # 以"id"为基准来删除重复值
                db = df.drop_duplicates(['id'])
                # 保存csv格式的数据
                db.to_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv')

#重新命名标题
def rename_column():
                try:
                    # 读取csv格式的数据
                    df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='gbk',index_col=0)
                    # 列的重命名
                    print(df.columns)
                    db = df.rename(columns={ 'id': 'ID'})
                    # 查看各列的名称
                    print(db.columns)
                    # 保存csv格式的数据
                    db.to_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv')
                except:
                    print("请输入正确的列名！")
                    print("wrong column name!")

#检查出现的重复电影个数
def cheak():
                # 读取csv格式的数据
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='gbk', index_col=0)
                # 判断重复数据记录
                a=list(df.duplicated())
                print("重复出现的电影个数：")
                print(a.count(True))
                print("预处理完成！")

start_read()
remove_duplicates()
cheak()
#修改列名
#rename_column()