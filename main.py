# Author: Lalitha Viswanathan
# Affiliation: Stanford HealthCare
# Samtools and flagstat parser
# from argparse import ArgumentParser
from argparse import ArgumentParser
from pprint import pprint

from flagstatutilities.flagstatutils import flagstat


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument('samtoolsfilename')
        parser.add_argument('sampleid')
        parser.add_argument('runid')
        args = parser.parse_args()
        (results, imagefile) = flagstat(args.samtoolsfilename)

        modifiedresults: dict[str, dict] = {'flagstat': {}}
        for key in results['flagstat'].keys():
            modifiedresults['flagstat'][key + "_percent_of_total_pf"] = (float(results['flagstat'][key]) / float(
                results['flagstat']['total_pf'])) * 100
        if imagefile:
            print(imagefile)
        pprint(modifiedresults)
    except Exception as exception:
        print("Error encountered calling samtools parser %s" % exception)
    finally:
        print("Samtools parser completed successfully")
############################################################
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
