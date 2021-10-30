import os

base_dir=os.path.dirname(os.path.abspath(__file__))

report_dir=os.path.join(base_dir,'report')

data_dir=os.path.join(base_dir,'data')

log_dir=os.path.join(base_dir,'log')

conifg_file_dir=os.path.join(base_dir,r'config_file'+'\Data_base_cf.ini')





# PROD_URL='https://apix.azazie.com/1.0'
PROD_URL='https://api-t-7.azazie.com'

TEST_URL='https://api-t-7.azazie.com'

def get_headers(token=None):
    header={"Content-Type":"application/json",
            "Accept":"application/json",
            "x-app":"pc",
            "x-token":"",
            "x-project":"azazie",
            "x-countryCode":"US"
            }
    if token:
        header["x-token"]=token[0]
    return header


