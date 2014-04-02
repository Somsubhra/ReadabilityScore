from scipy import stats
from os import path

# Generator class
class Generator:
    def __init__(self, asl, awl, asw, psw, psw30, juk, difficulty, output_directory):
        self.asl = asl
        self.awl = awl
        self.asw = asw
        self.psw = psw
        self.psw30 = psw30
        self.juk = juk
        self.difficulty = difficulty
        self.output_directory = output_directory

    def generate(self):
        corr_asl = stats.pearsonr(self.difficulty, self.asl)
        corr_awl = stats.pearsonr(self.difficulty, self.awl)
        corr_asw = stats.pearsonr(self.difficulty, self.asw)
        corr_psw = stats.pearsonr(self.difficulty, self.psw)
        corr_psw30 = stats.pearsonr(self.difficulty,self.psw30)
        corr_juk = stats.pearsonr(self.difficulty, self.juk)

        output_file = open(path.join(self.output_directory, 'result.csv'), 'a')

        output_file.write("\"\";\"\";\"\";\"\";\"\";\"\";\"\"\n")

        output_file.write("\"\";\"ASL\";\"AWL\";\"ASW\";\"PSW\";\"PSW30\";\"JUK\"\n")

        output_file.write("\"Correlation"
                          + "\";\""
                          + str(corr_asl[0])
                          + "\";\""
                          + str(corr_awl[0])
                          + "\";\""
                          + str(corr_asw[0])
                          + "\";\""
                          + str(corr_psw[0])
                          + "\";\""
                          + str(corr_psw30[0])
                          + "\";\""
                          + str(corr_juk[0])
                          + "\"\n")

        output_file.close()