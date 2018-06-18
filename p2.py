import sys
import nltk
import sklearn


def getText(filename):
    f = open(filename, 'r', encoding='UTF-8')
    return f.read()


def getVector(filename1, filename2):
    words = []
    words.append(" ".join(nltk.word_tokenize(getText(filename1))))
    words.append(" ".join(nltk.word_tokenize(getText(filename2))))

    countVector = sklearn.feature_extraction.text.CountVectorizer()

    vec = countVector.fit_transform(words)
    #print(vec.toarray())
    return sklearn.metrics.pairwise.cosine_similarity(vec[0], vec[1])


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    print('The content of '+file1+' is:\n'+getText(file1)+'\n')
    print('The content of '+file2+' is:\n'+getText(file2)+'\n\n')
    print('The cosine_similarity of '+file1+' and ' +
          file2+' is: '+str(getVector(file1, file2)[0][0]))


if __name__ == '__main__':
    main()
