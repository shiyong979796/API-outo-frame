import os
base_dir=os.path.dirname(os.path.abspath(__file__))
print(base_dir)

Token=None

PROD_URL='https://apix.azazie.com/1.0'



HEADER={
"Content-Type":"application/json",
"Accept":"application/json",
"x-app":"pc",#pc|android|ios|h5
# "x-token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYyNjU5Njk3NCwiZXhwIjoxNjI3MjAxNzc0LCJ1c2VyX2lkIjozODU2MDU4fQ.66bj19WYenhwfHZFqrWY5hO_EuwFxsMmue3-AOXzU-A",#用户token
"x-token":"{}".format(Token),
"x-project":"azazie",
"x-countryCode":""#US|CA 国家短码
}