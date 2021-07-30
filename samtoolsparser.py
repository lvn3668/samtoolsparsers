#!/usr/bin/env python3
# Author: Lalitha Viswanathan
# Samtools parser
# Affiliation: Stanford Health Care
import json
from argparse import ArgumentParser
from pprint import pprint

from flagstatutilities.flagstatutils import flagstat


############################################################
def is_json(myjson: json) -> bool:
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        print('invalid json: %s' % e)
        return False
    return True


############################################################
table_lookup: dict[str, str] = {
    'flagstat': 'samtools_flagstat'
}


############################################################
def parse_samtools_file(samtoolsfilename: str) -> str:
    try:
        resultsfromsamtoolsparser: dict = flagstat(samtoolsfilename)

        # Ouptut from samtools ; To be converted to percentage
        # {'flagstat': {'singletons_fail': '0', 'self_and_mate_pf': '1040733955', 'singletons_pf': '4163686', 'self_and_mate_fail': '0', 'properly_paired_pf': '984948647', 'total_fail': '0', 'different_chr_gt5_fail': '0', 'different_chr_pf': '18081440', 'duplicates_pf': '16871762', 'read1_pf': '525610111', 'paired_fail': '0', 'read2_pf': '525618053', 'different_chr_fail': '0', 'mapped_fail': '0', 'paired_pf': '1051228164', 'different_chr_gt5_pf': '3935380', 'mapped_pf': '1044897641', 'properly_paired_fail': '0', 'read2_fail': '0', 'duplicates_fail': '0', 'total_pf': '1051228164', 'read1_fail': '0'}}

        modifiedresults: dict[str, dict] = {'flagstat': {}}

        # for each key in flagstats, divide it by total_pf
        for key in resultsfromsamtoolsparser['flagstat'].keys():
            modifiedresults['flagstat'][key + "_percent_of_total_pf"] = (float(
                resultsfromsamtoolsparser['flagstat'][key]) / float(
                resultsfromsamtoolsparser['flagstat']['total_pf'])) * 100
        samtoolsparser: dict[str, dict[str, dict]] = {}
        if modifiedresults:
            samtoolsparser['modifiedresults'] = modifiedresults
        else:
            raise Exception('Modified Flagstat Results not generated correctly')

        if is_json(json.dumps(samtoolsparser)):
            return json.dumps(samtoolsparser)
        else:
            raise Exception('Invalid JSON: Samtools Flagstat')
    except Exception as exception:
        print("Error encountered parsing samtools output %s" % samtoolsparser)
    finally:
        print("Samtools parser completed")


############################################################


# 4198456 + 0 in total (QC-passed reads + QC-failed reads) 
# 0 + 0 duplicates 
# 4022089 + 0 mapped (95.80%:-nan%) 
# 4198456 + 0 paired in sequencing
# 2099228 + 0 read1 
# 2099228 + 0 read2 
# 3796446 + 0 properly paired (90.42%:-nan%)
# 4013692 + 0 with itself and mate mapped
# 8397 + 0 singletons (0.20%:-nan%)
# 167574 + 0 with mate mapped to a different chr
# 72008 + 0 with mate mapped to a different chr (mapQ>=5)
