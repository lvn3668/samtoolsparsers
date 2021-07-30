# Author: Lalitha Viswanathan
# Flagstat Utils
# Affiliation: Stanford Health Care
############################################################
from typing import re
############################################################
def flagstat(filename: str) -> dict:
    try:
        with open(filename) as f:
            text = f.read()
            # searches for
            # duplicates,
            # mapped pass/fail
            # paired pass/fail
            # read1 pass/fail
            # read2 pass/fail
            # properly paired reads pass/fail
            # self and mate pass/fail
            # singletons pass/fail
        pattern = r'(?P<total_pf>[0-9]+) \+ (?P<total_fail>[0-9]+) in total.*\n' \
                  + '(?P<duplicates_pf>[0-9]+) \+ (?P<duplicates_fail>[0-9]+) duplicates.*\n' \
                  + '(?P<mapped_pf>[0-9]+) \+ (?P<mapped_fail>[0-9]+) mapped.*\n' \
                  + '(?P<paired_pf>[0-9]+) \+ (?P<paired_fail>[0-9]+) paired.*\n' \
                  + '(?P<read1_pf>[0-9]+) \+ (?P<read1_fail>[0-9]+) read1.*\n' \
                  + '(?P<read2_pf>[0-9]+) \+ (?P<read2_fail>[0-9]+) read2.*\n' \
                  + '(?P<properly_paired_pf>[0-9]+) \+ (?P<properly_paired_fail>[0-9]+) properly.*\n' \
                  + '(?P<self_and_mate_pf>[0-9]+) \+ (?P<self_and_mate_fail>[0-9]+) with itself.*\n' \
                  + '(?P<singletons_pf>[0-9]+) \+ (?P<singletons_fail>[0-9]+) singletons.*\n' \
                  + '(?P<different_chr_pf>[0-9]+) \+ (?P<different_chr_fail>[0-9]+) with mate .*\n' \
                  + '(?P<different_chr_gt5_pf>[0-9]+) \+ (?P<different_chr_gt5_fail>[0-9]+) with mate.*\n'
        m = re.match(pattern, text)
        if not m:
            raise Exception('regex did not match')
    except (FileNotFoundError, IOError):
        print("Wrong file or file path")
    except Exception as exception:
        print("Exception encountered parsing flagstats %s" %exception)
    finally:
        print("Flagstat results parsed successfully")

        if not m.groupdict():
            raise Exception('Flagstat results not parsed correctly')

    results: dict[str, dict[str, str]] = {'flagstat': m.groupdict()}
    return results
############################################################