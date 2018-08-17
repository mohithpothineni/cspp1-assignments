'''
    Document Distance - A detailed description is given in the PDF
'''
def clean_up(strr):
    '''clean up as per inst...'''
    strr = strr.lower()
    strr_list = strr.split(' ')
    strr_list = [i.strip() for i in strr_list]
    strr_list = ["".join([k if (ord(k) in range(ord('a'), ord('z')+1))\
                else "" for k in i]) for i in strr_list]
    return strr_list



def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    cleaned_one = clean_up(dict1)
    cleaned_two = clean_up(dict2)

    stop_words = load_stopwords("stopwords.txt")
    cleaned_one = [i for i in cleaned_one if i not in stop_words]
    cleaned_two = [i for i in cleaned_two if i not in stop_words]

    freq_dict = {val:[cleaned_one.count(val), cleaned_two.count(val)]\
                for i, val in enumerate(cleaned_one) if i == cleaned_one.index(val)}

    for i in cleaned_two:
        if i not in freq_dict:
            freq_dict[i] = [0, cleaned_two.count(i)]
    freq_dict.pop("", 0)
    #print(sorted(freq_dict.keys()))
    numerator_ = sum([i[0]*i[1] for i in freq_dict.values()])
    denominator_ = ((sum([i[0]**2 for i in freq_dict.values()]))**0.5) *\
                   ((sum([i[1]**2 for i in freq_dict.values()]))**0.5)

    return 0 if denominator_ == 0 else numerator_ / denominator_

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
