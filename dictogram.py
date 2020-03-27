from random import randint, uniform


class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list

        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self):
        '''Creates a histogram dictionary using the word_list property and returns it'''
        diction = {}

        for i in self.word_list:
            if i in diction:
                diction[i] += 1
            else:
                diction[i] = 1
        return diction

        #TODO: use your histogram function as a starting point to complete this method
        pass

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram'''
        if word in self.dictionary_histogram:
            return self.dictionary_histogram[word]
        else:
            return 0
        pass

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        numwords = 0
        for i in self.dictionary_histogram:
            if self.dictionary_histogram[i] == 1:
                numwords += 1
        return numwords
        pass

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''
        lin = 0
        for key in self.dictionary_histogram:
            lin += self.dictionary_histogram[key]
        probval = []
        probdist = []
        for key in self.dictionary_histogram:
            probval.append(key)
            probdist.append(self.dictionary_histogram[key]/lin)
        return self.choice(probval, probdist)
        pass

    def choice(self, probval, probdist):
        r = uniform(0, 1)
        s = 0
        for i in range(0, len(probdist)):
            s += probdist[i]
            if s >= r:
                return probval[i]
        return probval

        def count(self, word):
            count = 0
            for i in self.dictionary_histogram:
                if i == word:
                    count += 1
            return count


if __name__ == "__main__":
    dicto = Dictogram("One fish two fish red fish blue fish".split(" "))
    sentence = []
    for i in range(10):
        sentence.append(dicto.sample())
    print(sentence)
