# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zQxZbUlRSCDKDe_HcQBYCdG5fTLIjc_k
"""

class MyMatrix:
    def __init__(self, data: list):
        
      self.__data = copy.deepcopy(data)


    def __repr__(self):
      
      kokos = ""
        
      for i in range(len(self.__data)):
        kokos = kokos + "\n"
        for ii in range(len(self.__data[i])):
          kokos = kokos + str(self.__data[i][ii])
          kokos = kokos + " "
         
      return kokos

    def size(self):
      m = self.__data
      width = 0
      lenght = 0
        
      for i in range (len(m)):
        width = width + 1
        for j in range (len(m[i])):
          lenght = lenght + 1
        
      aaa = (width, int(lenght/width))
      return aaa



    def flip_up_down(self):
      a = self.__data
      b = []
      for i in range(len(a)):
        b.append([])

      for i in range(len(a)):
        b[i] = a[len(a)-i-1]
      
      self.__data = b

    def flip_left_right(self):
      for i in range(len(self.__data)):
        for ii in range(len(self.__data[i])//2):
          self.__data[i][ii], self.__data[i][-ii - 1] = self.__data[i][-ii - 1], self.__data[i][ii]

          
    def flipped_up_down(self):
      a = self.__data
      b = []
      for i in range(len(a)):
        b.append([])

      for i in range(len(a)):
        b[i] = a[len(a)-i-1]
        
      kolya = MyMatrix(b)
      return kolya
    def flipped_left_right(self):
      
      x = self.__data
      for i in range(len(x)):
        for ii in range(x[i]//2):
          x[i][ii], x[i][-ii - 1] = x[i][-ii - 1], x[i][ii]
      kolya = MyMatrix(x)
      return kolya

    def transpose(self):
      
      if len(self.__data) != 0:   
        haha = [[0 for i in range(len(self.__data))] for ii in range(len(self.__data[0]))]
        for i in range(len(self.__data)):
          for ii in range(len(self.__data[i])):
            haha[ii][i] = self.__data[i][ii]
        self.__data = haha
      else: 
        self.data = []
    def transposed(self):
      sas = self.__data
      if len(sas) != 0:   
        haha = [[0 for i in range(len(sas))] for ii in range(len(sas[0]))]
        for i in range(len(sas)):
          for ii in range(len(sas[i])):
            haha[ii][i] = sas[i][ii]
        sas = haha
      else: 
        sas = []
      
      kolya = MyMatrix(sas)
      return kolya

    def __add__(self, other):
      
      if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
        haha = copy.deepcopy(self.__data)
        for i in range(len(self.__data)):
          for ii in range(len(self.__data[i])):
            haha[i][ii] += other.__data[i][ii]
            
        return MyMatrix(haha)
        
      else:
        raise NotImplementedError("ЗАЧЕМ ТЫ ВВЁЛ МАТРИЦЫ РАЗНОГО РАЗМЕРА, ИДИОТ??? У ТЕБЯ СИНДРОМ ДАУНА ЧТОЛИ???")

    def __iadd__(self, other):
      return self+other
    
    def __sub__(self, other):
      if len(self.__data) == len(other.__data) and len(self.__data[0]) == len(other.__data[0]):
        haha=copy.deepcopy(self.__data)
        for i in range(len(self.__data)):
          for j in range(len(self.__data[i])):
            haha[i][j] -= other.__data[i][j]
        return MyMatrix(haha)
      else:
        raise NotImplementedxError("ЗАЧЕМ ТЫ ВВЁЛ МАТРИЦЫ РАЗНОГО РАЗМЕРА, ИДИОТ??? У ТЕБЯ СИНДРОМ ДАУНА ЧТОЛИ???")

    def __isub__(self, other):  
      
      return self-other