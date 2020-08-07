import PyPluMA
import os

class SplitTableProcessingPlugin:
   def input(self, inputfile):
      filestuff = open(inputfile, 'r')
      self.firstline = filestuff.readline().strip().split('\t')
      self.classify = ["root", "kingdom", "phylum", "class", "order", "family", "genus", "species"]
      self.taxa = [[],[],[],[],[],[],[],[]]
      self.lines = [[],[],[],[],[],[],[],[]]
      rankID = self.firstline.index("rankID")
      taxon = self.firstline.index("taxon")
      for line in filestuff:
         # Classify lines first
         contents =line.strip().split('\t')
         rank = contents[rankID]
         tax = contents[taxon]
         self.lines[rank.count('.')].append(line)
         self.taxa[rank.count('.')].append(tax)

   def run(self):
      pass     

   def output(self, outputfile):
      samples = self.firstline
      samples.remove('taxlevel')
      samples.remove('rankID')
      samples.remove('taxon')
      samples.remove('daughterlevels')
      samples.remove('total')
      #samples.sort()
      newfirstline="\"\","
      for i in range(len(samples)):
         newfirstline += "\""+samples[i]+"\""
         if (i != len(samples)-1):
            newfirstline += ','
         else:
            newfirstline += '\n'

      directoryflag = False
      if (os.path.exists(PyPluMA.prefix()+"/kingdom")):
         directoryflag = True
         outputfile = outputfile.replace(PyPluMA.prefix(), '')

      for i in range(len(self.classify)):
         if (not directoryflag):
            filestuff =open(outputfile+"."+self.classify[i]+".csv", 'w')
         else:
            filestuff =open(PyPluMA.prefix()+"/"+self.classify[i]+"/"+outputfile+".csv", 'w')
         filestuff.write(newfirstline)
         for j in range(len(self.taxa[i])):
            mylines = self.lines[i]
            filestuff.write("\""+self.taxa[i][j]+"\""+",")
            contents = mylines[j].split('\t')
            contents = contents[5:]
            for k in range(len(contents)):
                  filestuff.write(contents[k])
                  if (k != len(contents)-1):
                     filestuff.write(',')
                  #else:
                  #   filestuff.write('\n')
                  
