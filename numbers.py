import random

with open("text2.txt", 'w') as f:
    
    f.write(('\n'.join([str(random.randint(0,32767)) for i in range(10000)])))   # randint(0, 32767) is equivalent to $RANDOM

f.close()
