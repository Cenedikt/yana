def http_encoder(sentence: str) -> str :
    '''
    encodes the querry into http frindy format
    takes : sentence as  string
    return string
    '''
    words = sentence.split()
    sentence = '%20'.join(words)

    return sentence

def http_decoder(sentence: str) -> str :
    '''
    decodes the back to sentence format
    takes : http query
    return string
    '''
    words = sentence.split('%20')
    sentence = ' '.join(words)

    return sentence
