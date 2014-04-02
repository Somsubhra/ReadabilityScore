import numpy as np
from scipy import stats
from os import path
from Parser import *


# Generator class
class Generator:

    # Constructor for generator class
    def __init__(self, asl, awl, asw, psw, psw30, juk30, difficulty, output_train_directory):
        self.asl = asl
        self.awl = awl
        self.asw = asw
        self.psw = psw
        self.psw30 = psw30
        self.juk30 = juk30
        self.difficulty = difficulty
        self.output_train_directory = output_train_directory

    # Generate the equation using linear regression
    def generate(self):

        print "Calculating correlations..."

        corr_asl = stats.pearsonr(self.difficulty, self.asl)
        corr_awl = stats.pearsonr(self.difficulty, self.awl)
        corr_asw = stats.pearsonr(self.difficulty, self.asw)
        corr_psw = stats.pearsonr(self.difficulty, self.psw)
        corr_psw30 = stats.pearsonr(self.difficulty,self.psw30)
        corr_juk30 = stats.pearsonr(self.difficulty, self.juk30)

        corr_asl_awl = stats.pearsonr(self.asl, self.awl)
        corr_asl_asw = stats.pearsonr(self.asl, self.asw)
        corr_asl_psw = stats.pearsonr(self.asl, self.asw)
        corr_asl_psw30 = stats.pearsonr(self.asl, self.psw30)
        corr_asl_juk30 = stats.pearsonr(self.asl, self.juk30)
        corr_awl_asw = stats.pearsonr(self.awl, self.asw)
        corr_awl_psw = stats.pearsonr(self.awl, self.psw)
        corr_awl_psw30 = stats.pearsonr(self.awl, self.psw30)
        corr_awl_juk30 = stats.pearsonr(self.awl, self.juk30)
        corr_asw_psw = stats.pearsonr(self.asw, self.psw)
        corr_asw_psw30 = stats.pearsonr(self.asw, self.psw30)
        corr_asw_juk30 = stats.pearsonr(self.asw, self.juk30)
        corr_psw_psw30 = stats.pearsonr(self.psw, self.psw30)
        corr_psw_juk30 = stats.pearsonr(self.psw, self.juk30)
        corr_psw30_juk30 = stats.pearsonr(self.psw30, self.juk30)

        output_file = open(path.join(self.output_train_directory, 'stats_training.csv'), 'a')

        output_file.write("\"\";\"\";\"\";\"\";\"\";\"\";\"\"\n")

        output_file.write("\"\";\"ASL\";\"AWL\";\"ASW\";\"PSW\";\"PSW30\";\"JUK30\"\n")

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
                          + str(corr_juk30[0])
                          + "\"\n")

        output_file.write("\"\";\"\";\"\";\"\";\"\";\"\";\"\"\n")

        output_file.write("\"\";\"ASL\";\"AWL\";\"ASW\";\"PSW\";\"PSW30\";\"JUK30\"\n")

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
                          + str(corr_asl_juk30[0])
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
                          + str(corr_awl_juk30[0])
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
                          + str(corr_asw_juk30[0])
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
                          + str(corr_psw_juk30[0])
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
                          + str(corr_psw30_juk30[0])
                          + "\"\n")
        output_file.write("\"JUK30"
                          + "\";\""
                          + str(corr_asl_juk30[0])
                          + "\";\""
                          + str(corr_awl_juk30[0])
                          + "\";\""
                          + str(corr_asw_juk30[0])
                          + "\";\""
                          + str(corr_psw_juk30[0])
                          + "\";\""
                          + str(corr_psw30_juk30[0])
                          + "\";\""
                          + "\"\n")

        output_file.close()

        self.features = []

        threshold = 0.4

        if abs(corr_asl[0]) > threshold:
            self.features.append('asl')
        if abs(corr_awl[0]) > threshold:
            self.features.append('awl')
        if abs(corr_asw[0]) > threshold:
            self.features.append('asw')
        #if abs(corr_psw[0]) > threshold:
        #    self.features.append('psw')
        if abs(corr_psw30[0]) > threshold:
            self.features.append('psw30')
        if abs(corr_juk30[0]) > threshold:
            self.features.append('juk30')

        print "Features selected", self.features

        features_data = []

        length = len(self.difficulty)

        for feature in self.features:
            if feature == 'asl':
                features_data.append(self.asl)
            elif feature == 'awl':
                features_data.append(self.awl)
            elif feature == 'asw':
                features_data.append(self.asw)
            elif feature == 'psw':
                features_data.append(self.psw)
            elif feature == 'psw30':
                features_data.append(self.psw30)
            elif feature == 'juk30':
                features_data.append(self.juk30)

        no_features = len(self.features)

        print "Performing linear regression using manual difficulty and selected features..."
        x = np.array(features_data, np.int32)

        y = np.array(self.difficulty)

        n = np.max(x.shape)

        X = np.vstack([np.ones(n), x]).T

        model, residue = np.linalg.lstsq(X, y)[:2]
        r2 = 1 - residue / (y.size * y.var())

        self.coeff = np.linalg.lstsq(X, y)[0]

        formula = ""
        for i in range(no_features):
            formula += "(" + str(self.coeff[i]) + ") * (" + str(self.features[i]) + ") + "

        formula += "(" + str(self.coeff[no_features]) + ")\nR^2 : " + str(r2)

        print "Generated the following formula: "
        print "---------------------------------------------------------------------------------"
        print formula
        print "---------------------------------------------------------------------------------"

    # Generate the custom index
    def custom_index(self, filename):

        self.parser = Parser(filename)

        length = len(self.features)

        index = 0.0

        feature_value = []
        for i in range(length):
            if self.features[i] == 'asl':
                index += float(self.parser.average_sentence_length()) * float(self.coeff[i])
            elif self.features[i] == 'awl':
                index += float(self.parser.average_word_length()) * float(self.coeff[i])
            elif self.features[i] == 'asw':
                index += float(self.parser.average_syllable_per_word()) * float(self.coeff[i])
            elif self.features[i] == 'psw':
                index += float(self.parser.number_of_polysyllables()) * float(self.coeff[i])
            elif self.features[i] == 'psw30':
                index += float(self.parser.number_of_polysyllables_per_30_sentences()) * float(self.coeff[i])
            elif self.features[i] == 'juk30':
                index += float(self.parser.number_of_jukthakshar_per_30_words()) * float(self.coeff[i])

        index += float(self.coeff[length])

        return index