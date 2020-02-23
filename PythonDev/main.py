# if True:
#     print("True")
# else:
#     print("False")

import json 

items = json.loads('[{"id":1, "text":"Item1"}, {"id":2, "text":"Item2"}]')

for item in items:
    print(item['text'])
    