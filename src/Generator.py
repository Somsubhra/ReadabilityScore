from scipy import stats

# Generate
class Generator:
    def __init__(self, asl, awl, asw, psw, psw30, juk, difficulty):
        self.asl = asl
        self.awl = awl
        self.asw = asw
        self.psw = psw
        self.psw30 = psw30
        self.juk = juk
        self.difficulty = difficulty

    def generate(self):
        corr_asl = stats.pearsonr(self.difficulty, self.asl)
        corr_awl = stats.pearsonr(self.difficulty, self.awl)
        corr_asw = stats.pearsonr(self.difficulty, self.asw)
        corr_psw = stats.pearsonr(self.difficulty, self.psw)
        corr_psw30 = stats.pearsonr(self.difficulty,self.psw30)
        corr_juk = stats.pearsonr(self.difficulty, self.juk)

        print corr_asl, corr_awl, corr_asw, corr_psw, corr_psw30, corr_juk