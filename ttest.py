import sys
import math
import time
import unicodedata
import argparse
import chrFplusplus
import numpy as np
from scipy.stats import ttest_ind

def main():
    #sys.stdout.write("start_time:\t%i\n" % (time.time()))


    argParser = argparse.ArgumentParser()
    argParser.add_argument("-srcl1", "--source_lang_1", help="source language 1", required=True)
    argParser.add_argument("-srcl2", "--source_lang_2", help="source language 2", required=True)
    argParser.add_argument("-nc", "--ncorder", help="character n-gram order (default=6)", type=int, default=6)
    argParser.add_argument("-nw", "--nworder", help="word n-gram order (default=2)", type=int, default=2)
    argParser.add_argument("-b", "--beta", help="beta parameter (default=2)", type=float, default=2.0)
    argParser.add_argument("-s", "--sent", help="show sentence level scores", action="store_true")

    args = argParser.parse_args()
    ref1_path = f"europarl-v7.{args.source_lang_1}-en-short.en"
    hyp1_path = f"{args.source_lang_1}-en-hyp.en"
    ref2_path = f"europarl-v7.{args.source_lang_2}-en-short.en"
    hyp2_path = f"{args.source_lang_2}-en-hyp.en"

    rtxt = open(ref1_path, 'r')
    htxt = open(hyp1_path, 'r')
    rtxt2 = open(ref2_path, 'r')
    htxt2 = open(hyp2_path, 'r')

    sentence_level_scores = None
    if args.sent:
        sentence_level_scores = sys.stdout # Or stderr?

    totalF, averageTotalF, totalPrec, totalRec, sent_scores = chrFplusplus.computeChrF(rtxt, htxt, args.nworder, args.ncorder, args.beta, sentence_level_scores)
    sent_scores_arr = np.array(sent_scores)

    totalF2, averageTotalF2, totalPrec2, totalRec2, sent_scores2 = chrFplusplus.computeChrF(rtxt2, htxt2, args.nworder,
                                                                                       args.ncorder, args.beta,
                                                                                       sentence_level_scores)
    sent_scores_arr2 = np.array(sent_scores2)
    sys.stdout.write(f"srcl1: {args.source_lang_1}\tc%i+w%i-F%i\t%.4f\n"  % (args.ncorder, args.nworder, args.beta, 100*totalF))
    sys.stdout.write(f"srcl1: {args.source_lang_1}\tc%i+w%i-avgF%i\t%.4f\n"  % (args.ncorder, args.nworder, args.beta, 100*averageTotalF))

    sys.stdout.write(f"srcl2: {args.source_lang_2}\tc%i+w%i-F%i\t%.4f\n" % (args.ncorder, args.nworder, args.beta, 100 * totalF2))
    sys.stdout.write(f"srcl2: {args.source_lang_2}\tc%i+w%i-avgF%i\t%.4f\n" % (args.ncorder, args.nworder, args.beta, 100 * averageTotalF2))
    #sys.stdout.write("c%i+w%i-Prec\t%.4f\n" % (args.ncorder, args.nworder, 100*totalPrec))
    #sys.stdout.write("c%i+w%i-Rec\t%.4f\n"  % (args.ncorder, args.nworder, 100*totalRec))
    stat, p = ttest_ind(sent_scores_arr, sent_scores_arr2)
    print(f"{args.source_lang_1}&{args.source_lang_2} p-value: {p}")

    #sys.stdout.write("end_time:\t%i\n" % (time.time()))

    htxt.close()
    rtxt.close()


if __name__ == "__main__":
    main()
