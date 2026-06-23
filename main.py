# e25eQ1- Coading challange

def read_inputs_from_txt_file(txt_filepath):
    with open(txt_filepath, 'r') as f:
        data = [line.strip() for line in f if line.strip()]
        H = int(data[0])
        C = int(data[1])
        preferences = data[2:]

        return H, C, preferences


def create_preferences_dict(preferences):
    cust_pref_dict = {}
    for i in range(0, len(preferences)):
        cust_pref_dict['C' + str(i)] = preferences[i].split(',')

    return cust_pref_dict


def update_itinerary(default_itinerary, dict_unsatisfied_cust):
    satisfied_cust_list = []

    for cust, pref in dict_unsatisfied_cust.items():
        for i in range(0, len(pref)):

            if pref[i].strip() in default_itinerary:
                print(f'customer {cust} is satisfied')
                satisfied_cust_list.append(cust)
                break

    for cust in satisfied_cust_list:
        dict_unsatisfied_cust.pop(cust)

    satisfied_cust_list = []
    for cust, pref in dict_unsatisfied_cust.items():
        for i in range(0, len(pref)):

            if 'airborne' in pref[i].strip().split(' '):
                hop_no = int(pref[i].strip().split(' ')[0])
                default_itinerary[hop_no] = f' {hop_no} airborne'
                print(f'customer {cust} is satisfied --> changed hop {hop_no} to airborne')
                satisfied_cust_list.append(cust)
                break

    for cust in satisfied_cust_list:
        dict_unsatisfied_cust.pop(cust)

    return default_itinerary, dict_unsatisfied_cust


def create_final_itinerary(H, cust_pref_dict):
    default_itinerary = [f'{i} by-sea' for i in range(H)]
    dict_unsatisfied_cust = {}
    dict_satisfied_cust = {}

    for cust, pref in cust_pref_dict.items():

        if len(pref) == 1 and 'airborne' in pref[0].split(' '):
            hop_no = int(pref[0].split(' ')[0])
            default_itinerary[hop_no] = pref[0]  # Set that perticular itn to airborne
            print(f'customer {cust} is satisfied --> unique airborne preference')
            dict_satisfied_cust.update({cust: pref})

        else:
            dict_unsatisfied_cust.update({cust: pref})

    while len(dict_unsatisfied_cust) > 0:
        default_itinerary, dict_unsatisfied_cust = update_itinerary(default_itinerary, dict_unsatisfied_cust)
        if default_itinerary == "NO ITINERARY":
            return "NO ITINERARY"

    print('all customers are satisfied')
    final_itinerary = default_itinerary

    return final_itinerary


if __name__ == '__main__':
    txt_filepath = r'input_data1.txt'

    H, C, preferences = read_inputs_from_txt_file(txt_filepath)
    cust_pref_dict = create_preferences_dict(preferences)

    final_itinerary = create_final_itinerary(H, cust_pref_dict)

    print('final_itinerary =', final_itinerary)
