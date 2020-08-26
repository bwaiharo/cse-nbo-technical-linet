import json
from collections import Counter 


with open('sample-json.json') as f:
  data = json.load(f)

label = list()
shape = list()
taggable_image = list()
points = list()

for d in data:
    taggable_image.append(d['taggable image'])
  
 

for t in taggable_image:
    for i in t:
        label.append(i['tags']['label'])
        shape.append(i['type'])
        points.append(i['points'])
   
def number_unique_shapes(s):
    return f"Unique Shapes {list(set(s))}. Number: {len(list(set(s)))}"

def frequency_of_shapes(l,s):
    cntr = Counter(list(zip(shape,label)))
    for x, y in cntr.items():
        print(f"Shape/Label: {x}, Count:{y}")

def visualization(l,s,p):
    return l,s,p

# if __name__ == '__main__':
    # print(visualization(label,shape,points))
    # print(points[0])
    # z=0
    # for i in range(len(points)):
    #     for p in points:
    #         print(p[i][0])
    #         z+=1
    #         print(z)
    # print(number_unique_shapes(shape))
    # print(frequency_of_shapes(label,shape))
  


# print(number_unique_shapes(shape))
# print(frequency_of_shapes(label,shape))

# print(f"shape {len(shape)}")
# print("------------------------")
# print(f"label {len(label)}")

# print(list(set(zip(shape,label))))
# print(Counter(list(zip(shape,label))))
