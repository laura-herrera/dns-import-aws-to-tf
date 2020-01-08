#!/usr/local/bin/python3

import sys
import route53

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <aws_hosted_zone_id> ...")
        sys.exit(1)

    conn = route53.connect(
            aws_access_key_id='<SOME_ACCESS_KEY>',
            aws_secret_access_key='<THE_SECRET>'
    )

    match_id = ''.join(sys.argv[1:])
    zone = conn.get_hosted_zone_by_id(match_id)
    print("# Imports for: " + match_id)
    print("")
    print("terraform import aws_route53_zone." + zone.name.replace(".", "_")[:-1] + " " + match_id)

    num_records = 0
    for record_set in zone.record_sets:
        num_records += 1
        tf_record_name = record_set.name.replace(".", "_")[:-1]
        print("terraform import aws_route53_record." + tf_record_name + " " + match_id + "_" + record_set.name[:-1] + "_" + record_set.rrset_type)

    print("# Num Records: " + str(num_records))
