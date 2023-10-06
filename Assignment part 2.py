# Task Two
# In the following, a code snippet featuring a list of dictionaries is provided. Please copy the code into a Python file, naming it as you prefer. Note that each dictionary contains four keys. Your task is to add an additional key, named “slug”, which will be populated using the “title” key. Below, sample output for each modified dictionary is presented.
#
# Sample Output

# {
# 'userId': 'Alex Gates',
# 'id': 5,
# 'title': ' nesciunt quas odio',
# 'body': 'repudiandae veniam quaerat sunt sed.....',
# 'slug': '-nesciunt-quas-odio'
# }

# Code need to copy
post_data = [
{
"userId": "Alex Gates",
"id": 1,
"title": "sunt aut facere repellat provident",
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": "Alex Gates",
"id": 2,
"title": "qui est esse ",
"body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
},
{
"userId": "Alex Gates",
"id": 3,
"title": "ea molestias quasi exercitationem ",
"body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
},
{
"userId": "Alex Gates",
"id": 4,
"title": "eum et est occaecati ",
"body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
},
{
"userId": "Alex Gates",
"id": 5,
"title": " nesciunt quas odio",
"body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
}]

# for user in post_data:
#     userid = user.get("userId")
#     id = user.get("id")
#     title = user.get("title")
#     body = user.get("body")
#     slug = title.lower().replace(' ','-').strip()

#     print(userid, id, title, body, slug, sep = ',\n')

for user in post_data:
    slug = user.get("title").replace(' ','-').strip()
    print(user, slug,'\n')
