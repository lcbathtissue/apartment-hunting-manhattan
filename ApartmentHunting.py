import random

num_apartments = random.randint(6, 36)
lim_fav_apartments = random.randint(2, num_apartments-1)

def gen_n_apartments(num_apartments):  # 10 .. 100 inclusive
    apartments = []
    while num_apartments > 0:
        apartments.append(random.randint(0, 1000)/10.0)
        num_apartments -= 1
    return apartments

apartments = gen_n_apartments(num_apartments)
apartments[0] = 14.3
print(f"apartments={apartments}")

def find_apartments():
    favorite_apartments = []
    print(f"favs={favorite_apartments}\n")
    for index, apartment in enumerate(apartments):
        if len(favorite_apartments) == 0:  # if no favorite apartments
            favorite_apartments.append(apartment)
            print(f"[{index}] {apartment} was added to favorites (Case 0)")
        else:
            best_apartment = favorite_apartments[-1]
            if apartment > best_apartment:  # if better apartment found
                favorite_apartments.append(apartment)
                print(f"[{index}] {apartment} was added to favorites")
                if len(favorite_apartments) == lim_fav_apartments:
                    print(f"\nSTOPPING BECAUSE NO MORE FAVORITES\n{favorite_apartments}")
                    return favorite_apartments
            else:
                print(f"[{index}] {apartment} was NOT a favorites because the best found apartment is {best_apartment}")
        print(f"favs={favorite_apartments}\n")
    print(f"\nSTOPPING BECAUSE NO MORE APARTMENTS\n{favorite_apartments}")
    return favorite_apartments

favorite_apartments = find_apartments()
