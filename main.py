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
    for i in range (0, len(preferences)):
        cust_pref_dict['C' + str(i)] = preferences[i].split(',')

    return cust_pref_dict


def update_itinerary(default_itinerary, dict_unsatisfied_cust):
    default_itinerary
    dict_unsatisfied_cust




    print('wait')

    return default_itinerary, dict_unsatisfied_cust





def create_final_itinerary(H, cust_pref_dict):

    default_itinerary = [f'{i} by-sea' for i in range(H)]

    for cust, pref in cust_pref_dict.items():
        dict_unsatisfied_cust= {}
        dict_satisfied_cust= {}
        dict_unsatisfied_cust.update({cust:[pref]})
        if len(pref) == 1:
            hop_no= int(pref[0].split(' ')[0])
            default_itinerary[hop_no] = pref[0] # Set that perticular itn to airborne
            print(cust, pref, 'satisfied')
            dict_satisfied_cust.update({cust: [pref]})

    dict_unsatisfied_cust

    update_itinerary(default_itinerary, dict_unsatisfied_cust)


    return default_itinerary



if __name__ == '__main__':
    txt_filepath = r'input_data.txt'

    H, C, preferences = read_inputs_from_txt_file(txt_filepath)
    cust_pref_dict= create_preferences_dict(preferences)

    final_itinerary = create_final_itinerary(H, cust_pref_dict)

    print('done')
