import pandas as pd



df = pd.read_csv('produkty.csv')
print(df['Product_name'].values)
total_kcal = int(input("Ile kcal chcesz zjesc łacznie?"))
print("Co chcesz zjeść")
product = input()

n = True
while product != 'n':
    prod_df = df.loc[df['Product_name'] == product]
    print(f"wybrałeś {product}")

    if prod_df['must_be_cooked'].values[0]:
        prod_df = df.loc[df['Product_name'] == product]
        print(f"Ile kcal {product} chcesz zjeść?")
        # zrobic tu try na bledna wartosc
        wanted_kcal = int(input())

        calc_raw = (100 / prod_df['raw_kcal'].values[0] * wanted_kcal).round()
        calc_cooked = (100 / prod_df['cooked_kcal'].values[0] * wanted_kcal).round()
        total_kcal = total_kcal - wanted_kcal



        print(f"{wanted_kcal} kcal {product} to:\n{calc_raw} g surowego\n{calc_cooked} g ugotowanego")

        print(f"Pozostało Ci {total_kcal} kcal")


        with open('eat_prod.txt', mode='a+') as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")

            f.write(f"{product} | {calc_raw} g sur i {calc_cooked} g ugo")

            # pozostalo ci
        # moze byc to zapisac do txt
    else:
        #
        print(f"Ile kcal {product} chcesz zjeść?")
        wanted_kcal = int(input())
        calc_raw = 100 / prod_df['raw_kcal'].values[0] * wanted_kcal
        print(f"{wanted_kcal} kcal {product} to:\n{calc_raw} g")
        total_kcal = total_kcal - wanted_kcal
        print(f"Pozostało Ci {total_kcal} kcal")

        with open('eat_prod.txt', mode='a+') as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")

            f.write(f"{product} | {calc_raw} ")


    print('Podaj kolejny produkt albo naciśnij n aby wyjść')
    product = input()
        #prod_df = df.loc[df['Product_name'] == product]













exit()

for product in df['Product_name'].values:

    if product == produkt:

        print("rowna sie")
    else:
        print("nierowna sie")

print("Ile kalorii")
wanted_kcals = input()

#check if product is needed to cook

# wartosc z dataframe






exit()
#
#
# print(products_df)
#
# # print("Podaj ile kcal w posilku")
# # all_req_kcal = int(input())
# # print(f"Podałes {all_req_kcal} na posilek, podaj produkt ")
#
# product = str(input())
#
# print("czy ma byc ugotowany?")
# value = input()
#
# if products_df.loc[products_df['Product_name'] == value]:
#      print("rowna sie")
# else:
#     print("nierowna")
#
#
# if input() == products_df['Product_name'].any:
#     print("Ile kcal chcesz zjesc ugotowanego produktu")
#     print(products_df['raw_kcal'].any)
#
#
#     # jak ma byc ugotowany to uzywamy dwoch kolumn (raw i cooked)
#
#
#     # a jak nie to jedna kolumna (raw)
#
#     one_kcal = 100/363 * 200
#     one_kcall = 100 / 75 * 200
#     cooked_one_kcal = 100/66 * 200
#     print(one_kcal)
#     print(cooked_one_kcal)
#     wanted_kcal_to_eat = int(input())
