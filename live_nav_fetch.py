






# Fetch NAV for 5 key schemes: 


import requests
import pandas as pd
import os


os.makedirs(
"data/raw/live_nav",
exist_ok=True
)


schemes = {
"SBI_Bluechip":119551,
"ICICI_Bluechip":120503,
"Nippon_Large_Cap":118632,
"Axis_Bluechip":119092,
"Kotak_Bluechip":120841
}


for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data=response.json()


    df=pd.DataFrame(data["data"])


    df["scheme_code"]=code
    df["scheme_name"]=data["meta"]["scheme_name"]


    file_name=f"data/raw/live_nav/{name}_nav.csv"


    df.to_csv(
        file_name,
        index=False
    )


    print(name,"saved")