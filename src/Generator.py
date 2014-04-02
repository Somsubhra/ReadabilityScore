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

        corr_asl_awl = stats.pearsonr(self.asl, self.awl)
        corr_asl_asw = stats.pearsonr(self.asl, self.asw)
        corr_asl_psw = stats.pearsonr(self.asl, self.asw)
        corr_asl_psw30 = stats.pearsonr(self.asl, self.psw30)
        corr_asl_juk = stats.pearsonr(self.asl, self.juk)
        corr_awl_asw = stats.pearsonr(self.awl, self.asw)
        corr_awl_psw = stats.pearsonr(self.awl, self.psw)
        corr_awl_psw30 = stats.pearsonr(self.awl, self.psw30)
        corr_awl_juk = stats.pearsonr(self.awl, self.juk)
        corr_asw_psw = stats.pearsonr(self.asw, self.psw)
        corr_asw_psw30 = stats.pearsonr(self.asw, self.psw30)
        corr_asw_juk = stats.pearsonr(self.asw, self.juk)
        corr_psw_psw30 = stats.pearsonr(self.psw, self.psw30)
        corr_psw_juk = stats.pearsonr(self.psw, self.juk)
        corr_psw30_juk = stats.pearsonr(self.psw30, self.juk)

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

        output_file.write("\"\";\"\";\"\";\"\";\"\";\"\";\"\"\n")

        output_file.write("\"\";\"ASL\";\"AWL\";\"ASW\";\"PSW\";\"PSW30\";\"JUK\"\n")

        output_file.write("\"ASL"
                          + "\";\""
                          + "\";\""
                          + str(corr_asl_awl[0])
                          + "\";\""
                          + str(corr_asl_asw[0])
                          + "\";\""
                          + str(corr_asl_psw[0])
                          + "\";\""
                          + str(corr_asl_psw30[0])
                          + "\";\""
                          + str(corr_asl_juk[0])
                          + "\"\n")
        output_file.write("\"AWL"
                          + "\";\""
                          + str(corr_asl_awl[0])
                          + "\";\""
                          + "\";\""
                          + str(corr_awl_asw[0])
                          + "\";\""
                          + str(corr_awl_psw[0])
                          + "\";\""
                          + str(corr_awl_psw30[0])
                          + "\";\""
                          + str(corr_awl_juk[0])
                          + "\"\n")
        output_file.write("\"ASW"
                          + "\";\""
                          + str(corr_asl_asw[0])
                          + "\";\""
                          + str(corr_awl_asw[0])
                          + "\";\""
                          + "\";\""
                          + str(corr_asw_psw[0])
                          + "\";\""
                          + str(corr_asw_psw30[0])
                          + "\";\""
                          + str(corr_asw_juk[0])
                          + "\"\n")
        output_file.write("\"PSW"
                          + "\";\""
                          + str(corr_asl_psw[0])
                          + "\";\""
                          + str(corr_awl_psw[0])
                          + "\";\""
                          + str(corr_asw_psw[0])
                          + "\";\""
                          + "\";\""
                          + str(corr_psw_psw30[0])
                          + "\";\""
                          + str(corr_psw_juk[0])
                          + "\"\n")
        output_file.write("\"PSW30"
                          + "\";\""
                          + str(corr_asl_psw30[0])
                          + "\";\""
                          + str(corr_awl_psw30[0])
                          + "\";\""
                          + str(corr_asw_psw30[0])
                          + "\";\""
                          + str(corr_psw_psw30[0])
                          + "\";\""
                          + "\";\""
                          + str(corr_psw30_juk[0])
                          + "\"\n")
        output_file.write("\"JUK"
                          + "\";\""
                          + str(corr_asl_juk[0])
                          + "\";\""
                          + str(corr_awl_juk[0])
                          + "\";\""
                          + str(corr_asw_juk[0])
                          + "\";\""
                          + str(corr_psw_juk[0])
                          + "\";\""
                          + str(corr_psw30_juk[0])
                          + "\";\""
                          + "\"\n")

        output_file.close()

        features = []

        if abs(corr_asl[0]) > 0.2:
            features.append('asl')
        if abs(corr_awl[0]) > 0.2:
            features.append('awl')
        if abs(corr_asw[0]) > 0.2:
            features.append('asw')
        if abs(corr_psw[0]) > 0.2:
            features.append('psw')
        if abs(corr_psw30[0]) > 0.2:
            features.append('psw30')
        if abs(corr_juk[0]) > 0.2:
            features.append('juk')

        print features

