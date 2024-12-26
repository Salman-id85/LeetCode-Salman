#import pakage
from typing import List
#overwriteing operation
class addsum:
  def toadd(self, nums : List[int],target : int) ->List[int]:
    dirc = {}
    for index,num in enumerate(nums):
      if target - num in dirc.keys():
        return [dirc[target - num],index]
      else:
        dirc[num] = index
#called 
demo = addsum()
result = demo.toadd([3,2,1,5], 8)
print(result)  #Output -> [0, 3]
