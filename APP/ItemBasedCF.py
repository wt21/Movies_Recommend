# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
 
# 基于项目的协同过滤推荐算法实现
import random
import pandas as pd
import math
from operator import itemgetter
import sys

class ItemBasedCF(object):
    ''' TopN recommendation - Item Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_movie = 20
        self.n_rec_movie = 10

        self.movie_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        # print('Similar movie number = %d' % self.n_sim_movie, file=sys.stderr)
        # print('Recommended movie number = %d' %
        #       self.n_rec_movie, file=sys.stderr)

    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        # data1=np.loadtxt(filename,delimiter=',',dtype=float)
        fp = open(filename, 'r', encoding='UTF-8')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if i % 100000 == 0:
            #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
        fp.close()
        print('load %s succ' % filename, file=sys.stderr)

    def generate_dataset(self, users, pivot=1.0):
        ''' load rating data and split it to training set and test set '''
        trainset_len = 0
        testset_len = 0

        for line in users:
            user = line.userId
            movie = line.movieId
            rating = line.rating
            # user, movie, rating = np.loadtxt(filename,delimiter=',')
         #   rating = float(rating)
            # print(type(rating))

            # split the data by pivot
            if random.random() < pivot:
                self.trainset.setdefault(user, {})

                self.trainset[user][movie] = rating
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})

                self.testset[user][movie] = rating
                testset_len += 1

        # print('split training set and test set succ', file=sys.stderr)
        print('train set = %s' % trainset_len, file=sys.stderr)
        # print('test set = %s' % testset_len, file=sys.stderr)
# 计算电影之间的相似度
    def calc_movie_sim(self):
        ''' calculate movie similarity matrix '''
        print('counting movies number and popularity...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for movie in movies:
                # count item popularity
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1

        # print('count movies number and popularity succ', file=sys.stderr)

        # save the total number of movies
        self.movie_count = len(self.movie_popular)
        print('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated users between items
        itemsim_mat = self.movie_sim_mat
        # print('building co-rated users matrix...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for m1 in movies:
                for m2 in movies:
                    if m1 == m2:
                        continue
                    itemsim_mat.setdefault(m1, {})
                    itemsim_mat[m1].setdefault(m2, 0)
                    itemsim_mat[m1][m2] += 1 / math.log(1 + len(movies) * 1.0)

        #print('build co-rated users matrix succ', file=sys.stderr)

        # calculate similarity matrix
        #print('calculating movie similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 2000000

        for m1, related_movies in itemsim_mat.items():
            for m2, count in related_movies.items():
                itemsim_mat[m1][m2] = count / math.sqrt(
                    self.movie_popular[m1] * self.movie_popular[m2])
                simfactor_count += 1
                if simfactor_count % PRINT_STEP == 0:
                    print('calculating movie similarity factor(%d)' %
                          simfactor_count, file=sys.stderr)

        #print('calculate movie similarity matrix(similarity factor) succ',
             # file=sys.stderr)
        #print('Total similarity factor number = %d' %
              #simfactor_count, file=sys.stderr)

    def recommend(self, user):
        ''' Find K similar movies and recommend N movies. '''
        matrix=[]
        #K = self.n_sim_movie
        #N = self.n_rec_movie
        K=3
        N=10
        matrix.clear()
        rank = {}
        watched_movies = self.trainset[user]

        for movie, rating in watched_movies.items():
            for related_movie, similarity_factor in sorted(self.movie_sim_mat[movie].items(),
                                                           key=itemgetter(1), reverse=True)[:K]:
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += similarity_factor * float(rating)
        # return the N best movies
        #print(sorted(rank.items(), key=itemgetter(1), reverse=True)[:N])
        rank_ = sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]
        for key,value in rank_:
            matrix.append(key)    #matrix为存储推荐的imdbId号的数组
            #print(key)     #得到了推荐的电影的imdbid号
        # print(matrix)
        #return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]
        return matrix


if __name__ == '__main__':
    rating_file = 'D:\\user_movie\\total.csv'
    userID='1'
    itemCF = ItemBasedCF()
    itemCF.generate_dataset(rating_file)
    itemCF.calc_movie_sim()
    #itemCF.evaluate()#推荐结果
    itemCF.recommend(userID)
    
    
