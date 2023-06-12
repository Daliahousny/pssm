import random
import math
import numpy as np
def calc_freq(seqs):
   count_A = 0
   count_C = 0
   count_G = 0
   count_T = 0
   freq_A = []
   freq_C = []
   freq_G = []
   freq_T = []
   big_list = []
   for pos in range(0, len(seqs[0])):
      for seq in seqs:
         if (seq[pos] == "A"):
            count_A += 1 / t
         elif (seq[pos] == "C"):
            count_C += 1 / t
         elif (seq[pos] == "G"):
            count_G += 1 / t
         elif (seq[pos] == "T"):
            count_T += 1 / t
      # count_A=round(count_A,2)
      freq_A.append(count_A)
      count_A = 0
      freq_C.append(count_C)
      count_C = 0
      # count_G=round(count_G,2)
      freq_G.append(count_G)
      count_G = 0
      freq_T.append(count_T)
      count_T = 0
   big_list.append(freq_A)
   big_list.append(freq_C)
   big_list.append(freq_G)
   big_list.append(freq_T)
   freq_matrix = np.array(big_list)
   return freq_matrix

def calc_tot(seqs):
   count_A = 0
   count_C = 0
   count_G = 0
   count_T = 0
   tot_list = []
   for pos in range(0, len(seqs[0])):
      for seq in seqs:
         if (seq[pos] == "A"):
            count_A += 1
         elif (seq[pos] == "C"):
            count_C += 1
         elif (seq[pos] == "G"):
            count_G += 1
         elif (seq[pos] == "T"):
            count_T += 1
   tot_list.append(count_A)
   tot_list.append(count_C)
   tot_list.append(count_G)
   tot_list.append(count_T)
   return tot_list

def calc_overall(tot_list):
   for i in range(0,len(tot_list)):
      tot_list[i]=round(tot_list[i]/tot_positions,3)
   return(tot_list)

def normalize(f, o):
   for i in range(len(f)):
      for j in range(len(f[i])):
         f[i][j] = round(f[i][j] / o[i], 2)
   return (f)

def log2(new_f):
   for i in range(len(new_f)):
      for j in range(len(new_f[i])):
         if (new_f[i][j] == 0):
            new_f[i][j] == "-"
         else:
            new_f[i][j] = round(math.log2(new_f[i][j]), 2)
   return new_f

def belong_to_family(normallized_matrix,seq):
    seq=seq.upper()
    total_score=0
    for i in range(len(seq)):
        if(seq[i]=='A'):
            total_score+=normallized_matrix[0][i]
        elif(seq[i]=='C'):
            total_score+=normallized_matrix[1][i]
        elif(seq[i]=='G'):
            total_score+=normallized_matrix[2][i]
        elif(seq[i]=='T'):            
            total_score+=normallized_matrix[3][i]
        else:
           print("you enter a non valid sequence!")
           return 0

    if(total_score<0):
        print("The score of the seq is: ",total_score)
        print("this sequence doesn't belong to the family!")
    else:
        print("The score of the seq is: ",total_score)
        print("this sequence fit the family well#")

print("a.run algorithm on file")
print("b.run algorithm on randomly generated sequences")
choice=input("Hello, please choose a or b ")
if (choice=='a'):
   path=input("Enter path of file data without double qoutes:")
   f = open(path, "r")
   lines = f.read().split()
   t = int(lines[0])  # no of sequences=5
   n = int(lines[1])  # no of characters in each sequence=8
   print("the multiple aligned sequences are:")
   seqs=[]
   for i in range(2,t+2):
      print(lines[i])
      seqs.append(lines[i].upper())
   print(seqs)
   tot_positions = t * n
   # print(tot_positions)
   freq_matrix=calc_freq(seqs)
   tot=calc_tot(seqs)
   overall=calc_overall(tot)
   normalized=normalize(freq_matrix,overall)
   pssm_matrix=log2(normalized)
   print("the pssm matrix is: \n",pssm_matrix)
   print("==========================================================================================================================================")
   seq=input("Enter the seq you want to check if it belong to the matrix:")
   belong_to_family(pssm_matrix,seq)
   print("==========================================================================================================================================")

elif(choice=='b'):
   randomm=[]
   t=int(input("please,Enter the number of sequences: "))
   n=int(input("And enter the length of seq: "))
   tot_positions=n*t
   nucleotides = ["A", "C", "G", "T"]
   for j in range(t):
      for i in range(t):
         seq = "".join(random.choices(nucleotides, k=n))
      randomm.append(seq)
   print("the multiple aligned sequences are :")
   print(randomm)
   freq_matrix=calc_freq(randomm)
   tot=calc_tot(randomm)
   overall=calc_overall(tot)
   normalized=normalize(freq_matrix,overall)
   pssm_matrix=log2(normalized)
   print("the pssm matrix is:")
   print(pssm_matrix)
   print("==========================================================================================================================================")
   seq=input("Enter the seq you want to check if it belong to the matrix:")
   l=len(seq)
   if(l>n):
      print("length of entered sequence exceeded limit")
   else:
      belong_to_family(pssm_matrix,seq)
      print("==========================================================================================================================================")

