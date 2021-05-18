import argparse
# from google.cloud import translate_v2 as translate
# from google.cloud import storage
from googletrans import Translator

def main(source_lang):
    #initialize translator
    print("Initializing Google Translate..")
    translator = Translator()

    ## PROCESS ITALIAN DATA, Take first 2000 lines and write to new file ##
    # print("Processing Italian data, writing to hypothesis file")
    # it_en_it = source_lang + "it-en/europarl-v7.it-en.it"
    # it_en_it_lines = open(it_en_it, "r").readlines()
    # it_en_it_lines_short = [it_en_it_lines[i] for i in range(100)]
    # it_en_it_short = open("europarl-v7.it-en-short.it", "x")
    # it_en_it_short.writelines(it_en_it_lines_short)
    # it_en_it_short.close()
    #
    # it_en_en = source_lang + "it-en/europarl-v7.it-en.en"
    # it_en_en_lines = open(it_en_en, "r").readlines()
    # it_en_en_lines_short = [it_en_en_lines[i] for i in range(100)]
    # it_en_en_short = open("europarl-v7.it-en-short.en", "x")
    # it_en_en_short.writelines(it_en_en_lines_short)
    #
    # print("beginning Italian translation..")
    # it_en_hyp_trans = translator.translate(it_en_it_lines_short, src='it', dest='en')
    # it_en_hyp_trans = [trans.text+'\n' for trans in it_en_hyp_trans]
    # it_en_hyp_file = open("it-en-hyp.en", "x")
    # it_en_hyp_file.writelines(it_en_hyp_trans)
    
    # ## PROCESS GERMAN DATA, Take first 2000 lines and write to new file ##
    # print("Processing German data, writing to hypothesis file")
    # de_en_de = source_lang + "de-en/europarl-v7.de-en.de"
    # de_en_de_lines = open(de_en_de, "r").readlines()
    # de_en_de_lines_short = [de_en_de_lines[i] for i in range(100)]
    # de_en_de_short = open("europarl-v7.de-en-short.de", "x")
    # de_en_de_short.writelines(de_en_de_lines_short)
    # de_en_de_short.close()
    #
    # de_en_en = source_lang + "de-en/europarl-v7.de-en.en"
    # de_en_en_lines = open(de_en_en, "r").readlines()
    # de_en_en_lines_short = [de_en_en_lines[i] for i in range(100)]
    # de_en_en_short = open("europarl-v7.de-en-short.en", "x")
    # de_en_en_short.writelines(de_en_en_lines_short)

    # print("beginning German translation..")
    # de_en_hyp_trans = translator.translate(de_en_de_lines_short, src='de', dest='en')
    # de_en_hyp_trans = [trans.text+'\n' for trans in de_en_hyp_trans]
    # de_en_hyp_file = open("de-en-hyp.en", "x")
    # de_en_hyp_file.writelines(de_en_hyp_trans)

    ## PROCESS GREEK DATA, WRITE TO FILE ##
    # print("Processing Greek data, writing to hypothesis file")
    # el_en_el = source_lang + "el-en/europarl-v7.el-en.el"
    # el_en_el_lines = open(el_en_el, "r").readlines()
    # el_en_el_lines_short = [el_en_el_lines[i] for i in range(100)]
    # el_en_el_short = open("europarl-v7.el-en-short.el", "x")
    # el_en_el_short.writelines(el_en_el_lines_short)
    # el_en_el_short.close()
    #
    # el_en_en = source_lang + "el-en/europarl-v7.el-en.en"
    # el_en_en_lines = open(el_en_en, "r").readlines()
    # el_en_en_lines_short = [el_en_en_lines[i] for i in range(100)]
    # el_en_en_short = open("europarl-v7.el-en-short.en", "x")
    # el_en_en_short.writelines(el_en_en_lines_short)
    #
    # print("beginning Greek translation..")
    # el_en_hyp_trans = translator.translate(el_en_el_lines_short, src='el', dest='en')
    # el_en_hyp_trans = [trans.text+'\n' for trans in el_en_hyp_trans]
    # el_en_hyp_file = open("el-en-hyp.en", "x")
    # el_en_hyp_file.writelines(el_en_hyp_trans)

    ## PROCESS FINNISH DATA, WRITE TO FILE ##
    # print("Processing Finnish data, writing to hypothesis file")
    # fi_en_fi = source_lang + "fi-en/europarl-v7.fi-en.fi"
    # fi_en_fi_lines = open(fi_en_fi, "r").readlines()
    # fi_en_fi_lines_short = [fi_en_fi_lines[i] for i in range(100)]
    # fi_en_fi_short = open("europarl-v7.fi-en-short.fi", "x")
    # fi_en_fi_short.writelines(fi_en_fi_lines_short)
    # fi_en_fi_short.close()
    #
    # fi_en_en = source_lang + "fi-en/europarl-v7.fi-en.en"
    # fi_en_en_lines = open(fi_en_en, "r").readlines()
    # fi_en_en_lines_short = [fi_en_en_lines[i] for i in range(100)]
    # fi_en_en_short = open("europarl-v7.fi-en-short.en", "x")
    # fi_en_en_short.writelines(fi_en_en_lines_short)
    #
    # print("beginning Finnish translation..")
    # fi_en_hyp_trans = translator.translate(fi_en_fi_lines_short, src='fi', dest='en')
    # fi_en_hyp_trans = [trans.text+'\n' for trans in fi_en_hyp_trans]
    # fi_en_hyp_file = open("fi-en-hyp.en", "x")
    # fi_en_hyp_file.writelines(fi_en_hyp_trans)

    ## PROCESS DUTCH DATA, WRITE TO FILE ##
    print("Processing Dutch data, writing to hypothesis file")
    nl_en_nl = source_lang + "nl-en/europarl-v7.nl-en.nl"
    nl_en_nl_lines = open(nl_en_nl, "r").readlines()
    nl_en_nl_lines_short = [nl_en_nl_lines[i] for i in range(100)]
    nl_en_nl_short = open("europarl-v7.nl-en-short.nl", "x")
    nl_en_nl_short.writelines(nl_en_nl_lines_short)
    nl_en_nl_short.close()

    nl_en_en = source_lang + "nl-en/europarl-v7.nl-en.en"
    nl_en_en_lines = open(nl_en_en, "r").readlines()
    nl_en_en_lines_short = [nl_en_en_lines[i] for i in range(100)]
    nl_en_en_short = open("europarl-v7.nl-en-short.en", "x")
    nl_en_en_short.writelines(nl_en_en_lines_short)

    print("beginning Dutch translation..")
    nl_en_hyp_trans = translator.translate(nl_en_nl_lines_short, src='nl', dest='en')
    nl_en_hyp_trans = [trans.text+'\n' for trans in nl_en_hyp_trans]
    nl_en_hyp_file = open("nl-en-hyp.en", "x")
    nl_en_hyp_file.writelines(nl_en_hyp_trans)

    print("Initial data processing completed")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_lang", "-sl", type=str, default="all")
    args = parser.parse_args()

    if args.source_lang == "all":
        args.source_lang = "data/"
    main(args.source_lang)