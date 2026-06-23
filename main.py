# e25eQ1- Coding Challange

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
        cust_pref_dict['C' + str(i)] = preferences[i].split(', ')

    return cust_pref_dict


def update_itinerary(default_itinerary, dict_unsatisfied_cust):
    satisfied_cust_list = []
    default_itinerary_changed = False

    for customer_id, pref in dict_unsatisfied_cust.items():
        for i in range(0, len(pref)):

            if pref[i].strip() in default_itinerary:
                print(f'customer {customer_id} is satisfied')
                satisfied_cust_list.append(customer_id)
                break

    for customer_id in satisfied_cust_list:
        dict_unsatisfied_cust.pop(customer_id)

    satisfied_cust_list = []
    for customer_id, pref in dict_unsatisfied_cust.items():
        for i in range(0, len(pref)):

            if 'airborne' in pref[i].strip().split(' '):
                hop_no = int(pref[i].strip().split(' ')[0])
                default_itinerary[hop_no] = f'{hop_no} airborne'
                default_itinerary_changed = True
                print(f'customer {customer_id} is satisfied --> changed hop {hop_no} to airborne')
                satisfied_cust_list.append(customer_id)
                break

    for customer_id in satisfied_cust_list:
        dict_unsatisfied_cust.pop(customer_id)

    if len(dict_unsatisfied_cust) > 0 and len(satisfied_cust_list) == 0 and default_itinerary_changed == False:
        return 'NO ITINERARY'

    return default_itinerary


def create_unsatisfied_customer_list(default_itinerary, customer_preferences_dict):
    unsatisfied_customers = {}
    for customer_id, pref in customer_preferences_dict.items():
        customer_satisfied = False

        for i in range(0, len(pref)):
            if pref[i].strip() in default_itinerary:
                customer_satisfied = True
                break
        if customer_satisfied == False:
            unsatisfied_customers[customer_id] = pref

    return unsatisfied_customers


def create_final_itinerary(H, cust_pref_dict):
    default_itinerary = [f'{i} by-sea' for i in range(H)]
    unsatisfied_customers = {}
    satisfied_customers = {}

    for cust, pref in cust_pref_dict.items():

        if len(pref) == 1 and 'airborne' in pref[0].split(' '):
            hop_no = int(pref[0].split(' ')[0])
            default_itinerary[hop_no] = pref[0]  # Set that perticular itn to airborne
            print(f'customer {cust} is satisfied --> unique airborne preference')
            satisfied_customers.update({cust: pref})

        else:
            unsatisfied_customers.update({cust: pref})

    while len(unsatisfied_customers) > 0:
        default_itinerary = update_itinerary(default_itinerary, unsatisfied_customers)
        if default_itinerary == "NO ITINERARY":
            return "NO ITINERARY"

        # If there are still unsatisfied customer because of this then please get the unsatisfied customer list

        unsatisfied_customers = create_unsatisfied_customer_list(default_itinerary, cust_pref_dict)

    print('all customers are satisfied')
    final_itinerary = default_itinerary

    return final_itinerary


if __name__ == '__main__':
    txt_filepath = r'input_data.txt'
    H, C, preferences = read_inputs_from_txt_file(txt_filepath)
    customer_preferences_dict = create_preferences_dict(preferences)
    final_itinerary = create_final_itinerary(H, customer_preferences_dict)

    print(final_itinerary)
