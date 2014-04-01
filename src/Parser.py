# Parser class
class Parser:

    # Constructor for parser class
    def __init__(self, filename):

        # Declaration of language specific lists

        separators = [u".", u"!", u"?"]

        halan = u'\u0acd'

        # Signs
        m_chandrabindu = u'\u0a81'
        m_anusvar = u'\u0a82'
        m_visarga = u'\u0a83'
        m_nukta = u'\u0abc'
        m_avagraha = u'\u0abd'

        # Independent vowels
        l_a = u'\u0a85'
        l_aa = u'\u0a86'
        l_i = u'\u0a87'
        l_ii = u'\u0a88'
        l_u = u'\u0a89'
        l_uu = u'\u0a8a'
        l_v_r = u'\u0a8b'
        l_v_l = u'\u0a8c'
        l_ae = u'\u0a8d'
        l_e = u'\u0a8f'
        l_ai = u'\u0a90'
        l_au = u'\u0a91'
        l_o = u'\u0a93'
        l_ow = u'\u0a94'

        # Consonant
        l_ka = u'\u0a95'
        l_kha = u'\u0a96'
        l_ga = u'\u0a97'
        l_gha = u'\u0a98'
        l_nga = u'\u0a99'
        l_ca = u'\u0a9a'
        l_cha = u'\u0a9b'
        l_ja = u'\u0a9c'
        l_jha = u'\u0a9d'
        l_nya = u'\u0a9e'
        l_tta = u'\u0a9f'
        l_ttha = u'\u0aa0'
        l_dda = u'\u0aa1'
        l_ddha = u'\u0aa2'
        l_nna = u'\u0aa3'
        l_ta = u'\u0aa4'
        l_tha = u'\u0aa5'
        l_da = u'\u0aa6'
        l_dha = u'\u0aa7'
        l_na = u'\u0aa8'
        l_pa = u'\u0aaa'
        l_pha = u'\u0aab'
        l_ba = u'\u0aac'
        l_bha = u'\u0aad'
        l_ma = u'\u0aae'
        l_ya = u'\u0aaf'
        l_ra = u'\u0ab0'
        l_la = u'\u0ab2'
        l_lla = u'\u0ab3'
        l_va = u'\u0ab5'
        l_sha = u'\u0ab6'
        l_ssa = u'\u0ab7'
        l_sa = u'\u0ab8'
        l_ha = u'\u0ab9'

        # Dependent vowels
        m_aa = u'\u0abe'
        m_i = u'\u0abf'
        m_ii = u'\u0ac0'
        m_u = u'\u0ac1'
        m_uu = u'\u0ac2'
        m_v_r = u'\u0ac3'
        m_v_rr = u'\u0ac4'
        m_ae = u'\u0ac5'
        m_e = u'\u0ac7'
        m_ai = u'\u0ac8'
        m_au = u'\u0ac9'
        m_o = u'\u0acb'
        m_ow = u'\u0acc'

        l_om = u'\u0ad0'
        l_ru = u'\u0af1'
        l_ri = u'\u0ae0'
        l_lri = u'\u0ae1'

        # Digits
        l_0 = u'\u0ae6'
        l_1 = u'\u0ae7'
        l_2 = u'\u0ae8'
        l_3 = u'\u0ae9'
        l_4 = u'\u0aea'
        l_5 = u'\u0aeb'
        l_6 = u'\u0aec'
        l_7 = u'\u0aed'
        l_8 = u'\u0aee'
        l_9 = u'\u0aef'

        # Consonants ordered based on the tongue action backward to forward
        ordered_consonants = [l_ha, l_a, l_ka, l_ga, l_kha, l_gha, l_ca, l_cha, l_ja, l_cha, l_sha, l_jha, l_ssa, l_nya,
                              l_ya, l_dda, l_ddha, l_ttha, l_tta, l_na, l_la, l_ra, l_sa, l_ta, l_da, l_dha, l_tha,
                              l_nna, l_lla, l_nga, l_pha, l_va, l_ma, l_bha, l_ba, l_pa]

        self.filename = filename

        # Read the contents of file as UTF-8
        self.contents = open(filename).read()
        self.contents = self.contents.decode("utf-8")

        # Store all words of content
        self.words = self.contents.split()

        # Calculate number of words
        self.no_words = len(self.words)

        # Calculate number of sentences
        self.no_sentences = 0

        # Calculate the average word length
        self.avg_word_l = 0

        # Calculate number of jukthakshars
        self.no_jukthakshar = 0

        self.stripped_words = []

        for word in self.words:
            if word[-1] in separators and len(word) > 1:
                self.no_sentences += 1

            self.avg_word_l += float(len(word)) / float(self.no_words)

            if halan in word:
                self.no_jukthakshar += word.count(halan)

            self.stripped_words.append(''.join([s for s in word if s in ordered_consonants]))

        if self.no_sentences == 0:
            self.no_sentences = 1

    # Number of words in the content
    def number_of_words(self):
        return self.no_words

    # Number of sentences in the content
    def number_of_sentences(self):
        return self.no_sentences

    # Average number of words per sentence
    def average_words_per_sentence(self):
        return float(self.no_words) / float(self.no_sentences)

    # Average word length
    def average_word_length(self):
        return self.avg_word_l

    # Calculate number of jukthakshars
    def number_of_jukthakshar(self):
        return self.no_jukthakshar