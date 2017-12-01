from __future__ import division
from math import sqrt
from kFold import kFold as fungsi
import random


LearnData = []

class F:
    def __init__(self,fit,K):
        self.fit = fit
        self.K = K
class Data:
    def __init__(self,nomor,like,provokasi,komentar,emosi,hoax):
        self.nomor = nomor
        self.like = like
        self.provokasi =provokasi
        self.komentar = komentar
        self.emosi = emosi
        self.hoax = hoax
class ResultClass:
    def __init__(self, distance, data):
        self.distance = distance
        self.data = data
with open('Dataset/data.csv', 'r') as f:
    reader1 = csv.reader(f)
    for row in reader1:
        LearnData.append(Data(row[0], row[1], row[2],row[3],row[4],row[5]))
def find(item, arr):
    for i in range(len(arr)):
        if arr[i]==item:
            return True
    return False
def Test(Learn_Data, Test_Data):
    distance  = sqrt((int(Learn_Data.provokasi)-int(Test_Data.provokasi))**2 + (int(Learn_Data.like)-int(Test_Data.like))**2 + (int(Learn_Data.komentar)-int(Test_Data.komentar))**2 + (int(Learn_Data.emosi)-int(Test_Data.emosi))**2)
    Result = ResultClass(distance, Learn_Data)
    return Result
def GetClassification(K, Result):
    Count_Ya = 0
    Count_Tidak = 0
    i=0
    while (i<K):
        # print len(DataResult),i
        if (Result[i].data.hoax == "1"):
            Count_Ya +=1
        else:
            Count_Tidak +=1
        i+=1

    # print Count_Ya, Count_Tidak
    if (Count_Ya > Count_Tidak):
        return "1"
    else:
        return "0"
def fungsi(K):
    index_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rata2 = 0
    no = 1

    while not (index_test[0] > len(LearnData) - 1):
        akurasi = 0
        count = 0

        for i in range(len(index_test)):
            Result = []
            for j in range(len(LearnData)):
                if not find(j, index_test):
                    Result.append(Test(LearnData[j], LearnData[index_test[i]]))
            Result.sort(key=lambda ResultClass: ResultClass.distance, reverse=False)
            # print DataResult[0].distance,DataResult[1].distance
            if LearnData[index_test[i]].hoax == GetClassification(K, Result):
                count += 1

        akurasi = (count / len(index_test)) * 100
        rata2 += akurasi
        no += 1
        for _ in range(len(index_test)):
            index_test[_] += 10

    return rata2 / (no-1)

def genPopulasi(nPop, nKrom):
    pop = [[int(round(random.random())) for i in range(nKrom)] for j in range(nPop)]
    return pop
def randomParent(nPop):
    return int(round(random.uniform(0,nPop)))
def hitungFitness(krom):
    K= 0
    for i in range(len(krom)):
        if krom[i]==1:
            K +=2**i * krom[i]

    fit = fungsi(K)
    fitness = F(fit,K)
    return fitness

if  __name__ == '__main__':
    pCross = 0.8
    pMutasi =0.1
    nPop = 9
    nGen = 5
    nKrom = 10
    pop =genPopulasi(nPop,nKrom)

    for i in range(nGen):

        anak = []
        fitness =[]

        for j in range(nPop % 2):
            # Seleksi orang tua
            parent1 = randomParent(nPop-1)
            parent2 = randomParent(nPop-1)

            anak1 =pop[parent1][:]
            anak2 =pop[parent2][:]
            # Crossover
            rand = random.random()
            titik= int(round(random.uniform(0,nKrom-1)))
            if rand <=pCross:
                #print titik
                #print anak1, anak2
                for k in range(titik):
                    anak1[k],anak2[k] = anak2[k], anak1[k]

            rand = random.random()
            titik = int (round(random.uniform(0,nKrom-1)))
            if rand<=pMutasi:
                if anak1[titik]==0:
                    anak1[titik] = 1
                else:
                    anak1[titik] = 0

            rand = random.random()
            titik = int(round(random.uniform(0, nKrom - 1)))
            if rand <= pMutasi:
                if anak2[titik] == 0:
                    anak2[titik] = 1
                else:
                    anak2[titik] = 0

            anak.append(anak1)
            anak.append(anak2)

        gab = pop + anak
        for j in range(len(gab)):
            fit = hitungFitness(gab[j])
            if (fitness==[] or fit.fit>fitness[0].fit ):
                fitness.append(fit)

        pop = []
        pop = genPopulasi(nPop,nKrom)
        # print pop

print "Akurasi,K:", fitness[0].fit,fitness[0].K