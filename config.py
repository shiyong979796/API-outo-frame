import os

base_dir=os.path.dirname(os.path.abspath(__file__))

report_dir=os.path.join(base_dir,'report')

data_dir=os.path.join(base_dir,'data')

log_dir=os.path.join(base_dir,'log')

conifg_file_dir=os.path.join(base_dir,r'config_file'+'\Data_base_cf.ini')


# PROD_URL='https://apix.azazie.com/1.0'
PROD_URL='https://api-t-7.azazie.com'

TEST_URL='https://api-t-7.azazie.com'
HEADER={
"Content-Type":"application/json",
"Accept":"application/json",
"x-app":"pc",#pc|android|ios|h5
# "x-token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYyNjU5Njk3NCwiZXhwIjoxNjI3MjAxNzc0LCJ1c2VyX2lkIjozODU2MDU4fQ.66bj19WYenhwfHZFqrWY5hO_EuwFxsMmue3-AOXzU-A",#用户token
"x-token":"",
"x-project":"azazie",
"x-countryCode":""#US|CA 国家短码
}