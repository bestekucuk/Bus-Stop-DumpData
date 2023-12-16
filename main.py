import pandas as pd

df = pd.read_csv('durak.csv')

# unique_names = df['DURAK_ADI'].unique()
# test_dict = {}
# for item in unique_names:
    
duraktan_gecen_hat = df.loc[df['HAT_NO'] == 5, 'DURAK_ADI'].unique()
print(duraktan_gecen_hat)
#     durak_no = df.loc[df['DURAK_ADI'] == item, 'DURAK_ID'].unique()[0]
#     # duraktan_gecen_hat_ismi = df.loc[df['DURAK_ADI'] == item, 'DURAK_ADI'].unique()
#     tempt = {
#         "NAME":item,
#         "HATLAR":duraktan_gecen_hat
#     }
#     test_dict[durak_no] = tempt

# for keys,value in test_dict.items():
#     print(f"durak ismi : {value['NAME']} durak no : {keys}    geçen hatlar: {value['HATLAR']}")

# df = pd.read_csv('saatler.csv')
# unique_names = df['HAT_NO'].unique()
# new_list =  []
# for item in unique_names:
#     gidis_saati = df.loc[(df['HAT_NO'] == item) & (df['TARIFE_ID'] == 1), 'GIDIS_SAATI'].tolist()
#     varis_saati = df.loc[(df['HAT_NO'] == item) & (df['TARIFE_ID'] == 1), 'DONUS_SAATI'].tolist()
#     tempt = {
#         "HAT_NO":item,
#         "KALKIS" : gidis_saati,
#         "VARIS": varis_saati
#     }
#     new_list.append(tempt)

# for item in new_list:
#     if item['HAT_NO'] == 5 or item['HAT_NO'] == "5":
#         print(f"HAT NO: {item['HAT_NO']}  \n KALKIS SAATLERİ  {item['KALKIS']}  \n  \nvaris   {item['VARIS']} \n\n")
#         print("toplam sefer sayısı ", len(item['KALKIS']))
#         print("toplam var sayısı ", len(item['VARIS']))