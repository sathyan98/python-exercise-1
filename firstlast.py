def alpha(str):
      ctr = 0
      for word in str:
          if len(word) > 1 and word[0] == word[-1]:
              ctr += 1
      return ctr



print(alpha(['abc','xyz','aba','1221']))

















#  Sample List : ['abc', 'xyz', 'aba', '1221']
#    Expected Result : 2