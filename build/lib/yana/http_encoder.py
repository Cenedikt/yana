def http_encoder(sentence: str) -> str :
    '''
    encodes the querry into http frindy format
    takes : sentence as  string
    return string
    '''
    words = sentence.split()
    sentence = '%20'.join(words)

    return sentence
