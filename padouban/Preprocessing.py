# coding=gbk
import pandas as pd
#�鿴����
def start_read():
                # ��ȡcsv��ʽ������
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='utf-8',index_col=0)
                # �鿴����ά��
                print(df.shape)
                # �鿴������Ϣ
                print(df.info() )
                # �鿴���е�����
                print(df.columns )
                # �鿴�е���������
                print(df['id'].dtype)

#ȥ���ظ�ֵ
def remove_duplicates():    #ȥ���ظ�ֵ
                # ��ȡcsv��ʽ������
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='utf-8',index_col=0)
                # ɾ�����п�ֵ����
                df.dropna(how='any')
                # �ж��ظ����ݼ�¼
                isDuplicated = df.duplicated()
                print(isDuplicated)
                # ��"id"Ϊ��׼��ɾ���ظ�ֵ
                db = df.drop_duplicates(['id'])
                # ����csv��ʽ������
                db.to_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv')

#������������
def rename_column():
                try:
                    # ��ȡcsv��ʽ������
                    df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='gbk',index_col=0)
                    # �е�������
                    print(df.columns)
                    db = df.rename(columns={ 'id': 'ID'})
                    # �鿴���е�����
                    print(db.columns)
                    # ����csv��ʽ������
                    db.to_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv')
                except:
                    print("��������ȷ��������")
                    print("wrong column name!")

#�����ֵ��ظ���Ӱ����
def cheak():
                # ��ȡcsv��ʽ������
                df = pd.read_csv('C:\\Users\\53581\\Desktop\\doubanpachong.csv', encoding='gbk', index_col=0)
                # �ж��ظ����ݼ�¼
                a=list(df.duplicated())
                print("�ظ����ֵĵ�Ӱ������")
                print(a.count(True))
                print("Ԥ������ɣ�")

start_read()
remove_duplicates()
cheak()
#�޸�����
#rename_column()