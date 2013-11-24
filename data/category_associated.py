import nltk

class Descrption:
    ...
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    ...
    def normalized_words(self, article_text):
        words   = []
        oneline = article_text.replace('\n', ' ')
        cleaned = nltk.clean_html(oneline.strip())
        toks1   = cleaned.split()
        for t1 in toks1:
            translated = self.regex.sub('', t1)
            toks2 = translated.split()
            for t2 in toks2:
                t2s = t2.strip().lower()
                if self.stop_words.has_key(t2s):
                    pass
                else:
                    words.append(t2s)
        return words
