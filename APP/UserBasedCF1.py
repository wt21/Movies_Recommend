# -*- coding: utf-8 -*-
 
# 基于用户的协同过滤推荐算法实现
import random
import pandas as pd
import math
from operator import itemgetter
import sys

user_sim_mat = {}

class UserBasedCF(object):
    ''' TopN recommendation - User Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}  # 训练集
        self.testset = {}  # 测试集
        self.initialset = {}  # 存储要推荐的用户的信息
        self.n_sim_user = 30
        self.n_rec_movie = 10

        self.movie_popular = {}
        self.movie_count = 0  # 总电影数量

        print('Similar user number = %d' % self.n_sim_user, file=sys.stderr)
        print('recommended movie number = %d' %
              self.n_rec_movie, file=sys.stderr)
    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        fp = open(filename, 'r', encoding='UTF-8')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if i % 100000 == 0:
            #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
        fp.close()
        print('load %s success' % filename, file=sys.stderr)

    #数据读取函数
    def initial_dataset(self, filename1):
        initialset_len = 0
        for lines in self.loadfile(filename1):
            users, movies, ratings = lines.split(',')
            self.initialset.setdefault(users, {})
            self.initialset[users][movies] = (ratings)
            initialset_len += 1

    def generate_dataset(self, users, pivot=1.0):
        ''' load rating data and split it to training set and test set '''
        trainset_len = 0
        testset_len = 0

        for line in users:
            user = line.userId
            movie = line.movieId
            rating = line.rating
            # split the data by pivot
            if random.random() < pivot:  # pivot=0.7应该表示训练集：测试集=7：3
                self.trainset.setdefault(user, {})
                self.trainset[user][movie] = (rating)  # trainset[user][movie]可以获取用户对电影的评分  都是整数
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})
                self.testset[user][movie] = (rating)
                testset_len += 1

        print('split training set and test set successful!', file=sys.stderr)
        print('train set = %s' % trainset_len, file=sys.stderr)
        print('test set = %s' % testset_len, file=sys.stderr)

    def UserSimilarity(self):
        #建立物品-用户的倒排表
        #数据格式：key:物品 value:用户1，用户2
        movie2users = dict()
        #遍历训练集中用户-物品数据
        for user, movies in self.trainset.items():
            #遍历用户对应的物品数据
            for movie in movies:
                # inverse table for item-users
                if movie not in movie2users: #倒排表还没有该物品
                    movie2users[movie] = set()#倒排表中该物品项赋值为set()集合
                movie2users[movie].add(user)  #倒排表中该物品项添加该用户
                
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        # print ('build movie-users inverse table succ', file=sys.stderr)

        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)
        print('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated items between users  计算用户之间共同评分的物品
        usersim_mat = user_sim_mat
        # print ('building user co-rated movies matrix...', file=sys.stderr)

        for movie, users in movie2users.items():  # 通过.items()遍历movie2users这个字典里的所有键、值
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    usersim_mat.setdefault(u, {})
                    usersim_mat[u].setdefault(v, 0)
                    usersim_mat[u][v] += 1 / math.log(1 + len(users))  # usersim_mat二维矩阵应该存的是用户u和用户v之间共同评分的电影数目
        
        simfactor_count = 0

        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count / math.sqrt(
                    len(self.trainset[u]) * len(self.trainset[v]))
                simfactor_count += 1

#用户user未产生过行为的物品
                
    def recommend(self, user):
        ''' Find K similar users and recommend N movies. '''
        matrix=[]  
        K = self.n_sim_user  # 这里等于20
        N = self.n_rec_movie  # 这里等于10
        rank = dict()  # 用户对电影的兴趣度
        # print(self.initialset[user])
        watched_movies = self.trainset[user]  # user用户已经看过的电影  只包括训练集里的
        # 这里之后不能是训练集
        # watched_movies = self.initialset[user]
        for similar_user, similarity_factor in sorted(user_sim_mat[user].items(),
                                                      key=itemgetter(1), reverse=True)[
                                               0:K]:  # itemgetter(1)表示对第2个域(相似度)排序   reverse=TRUE表示降序
            for imdbid in self.trainset[similar_user]:  # similar_user是items里面的键，就是所有用户   similarity_factor是值，就是对应的相似度
                if imdbid in watched_movies:
                    continue  # 如果该电影用户已经看过，则跳过
                rank.setdefault(imdbid, 0)  # 没有值就为0
                rank[imdbid] += similarity_factor   #rank[movie]就是各个电影的相似度
                # 这里是把和各个用户的相似度加起来，而各个用户的相似度只是基于看过的公共电影数目除以这两个用户看过的电影数量积
                #print(rank[movie])
        # return the N best movies
       # rank_ = dict()
        rank_ = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]  #类型是list不是字典了
        for key,value in rank_:
            matrix.append(key)    #matrix为存储推荐的imdbId号的数组
            #print(key)     #得到了推荐的电影的imdbid号
        print(matrix)
        #return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
        return matrix
    
if __name__ == '__main__':
    rating_file = 'C:\\Users\\tong\\Desktop\\movies\\ml-latest-small\\rating.csv'
    userID=input('请输入用户编号：')
    userCF = UserBasedCF()
    userCF.generate_dataset(rating_file)
    userCF.UserSimilarity()
    print('为该用户推荐的评分最高的10部电影是：'.center(30, '='))
    userCF.recommend(userID)#推荐结果

