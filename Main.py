from math import sqrt
import csv

# Global Variable
TestData = []
LearnData = []

class Data:
    def __init__(self,nomor,like,provokasi,komentar,emosi,hoax=None):
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
with open('Datatrain/data.csv', 'r') as g:
    reader2 = csv.reader(g)
    for row in reader2:
        TestData.append(Data(row[0], row[1], row[2],row[3],row[4]))


def Test(Learn_Data, Test_Data):
    distance  = sqrt((int(Learn_Data.provokasi)-int(Test_Data.provokasi))**2 + (int(Learn_Data.like)-int(Test_Data.like))**2 + (int(Learn_Data.komentar)-int(Test_Data.komentar))**2 + (int(Learn_Data.emosi)-int(Test_Data.emosi))**2)
    Result = ResultClass(distance, Learn_Data)
    return Result
def GetClassification(K, Result):
    Count_Ya = 0
    Count_Tidak = 0
    for i in range(K):
        if (Result[i].data.hoax == "1"):
            Count_Ya +=1
        else:
            Count_Tidak +=1

    # print Count_Ya, Count_Tidak
    if (Count_Ya > Count_Tidak):
        return "Ya"
    else:
        return "Tidak"

if __name__ == '__main__':
    K = 21

    for i in range(len(TestData)):
        Result = []
        for j in range(len(LearnData)):
            Result.append(Test(LearnData[j],TestData[i]))
        Result.sort(key=lambda ResultClass: ResultClass.distance,reverse=False)
        TestData[i].hoax = GetClassification(K, Result)
        print TestData[i].nomor,TestData[i].like,TestData[i].provokasi,TestData[i].komentar,TestData[i].emosi,TestData[i].hoax

    with open('DataResult/result.csv', 'w') as r:
        writer = csv.writer(r)
        for _ in range(len(TestData)):
            writer.writerow({TestData[i].nomor,TestData[i].like,TestData[i].provokasi,TestData[i].komentar,TestData[i].emosi,TestData[i].hoax})