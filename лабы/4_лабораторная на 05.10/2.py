import math
import datetime
import my_module
from my_module import count_points_cybernitic
name = input()
number = input()
my_module.the_best_function(name)

dt = datetime.datetime.now().time()
end = count_points_cybernitic(name, str(dt), math.sqrt(int(number)), int(number[::-1]))
print(end % 50)