#!/usr/local/bin/python3

import sys
import route53

def a_record(record_set):
    print("resource \"aws_route53_record\" \"" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"A\"")
    print("    ttl = \"300\"")
    if len(record_set.records) == 1:
        print("    records = [\"" + ''.join(record_set.records) + "\"]")
    else:
        print("    records = [\"" + '\", \"'.join(record_set.records) + "\"]")
    print("}")
    print("")

def txt_record(record_set):
    print("resource \"aws_route53_record\" \"" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"TXT\"")
    print("    ttl = \"300\"")
    print("    records = [" + ''.join(record_set.records) + "]")
    print("}")
    print("")

def mx_record(record_set):
    print("resource \"aws_route53_record\" \"mx_" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"MX\"")
    print("    ttl = \"300\"")
    print("    records = [\"" + ''.join(record_set.records) + "\"]")
    print("}")
    print("")

def alias_record(record_set):
    print("resource \"aws_route53_record\" \"" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"A\"")
    print("    alias {")
    print("        name = \"" + record_set.alias_dns_name + "\"")
    print("        zone_id = \"" + record_set.alias_hosted_zone_id + "\"")
    print("        evaluate_target_health = false")
    print("    }")
    print("}")
    print("")

def cname_record(record_set):
    print("resource \"aws_route53_record\" \"" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"CNAME\"")
    print("    ttl = \"300\"")
    print("    records = [\"" + ''.join(record_set.records) + "\"]")
    print("}")
    print("")

def ns_record(record_set):
    print("resource \"aws_route53_record\" \"" + record_set.name.replace(".", "_")[:-1] + "\" {")
    print("    zone_id = aws_route53_zone." + zone.name.replace(".", "_")[:-1] + ".zone_id")
    print("    name = \"" + record_set.name[:-1] + "\"")
    print("    type = \"NS\"")
    print("    ttl = \"300\"")
    if len(record_set.records) == 1:
        print("    records = [" + ''.join(record_set.records) + "]")
    else:
        print("    records = [\"" + '\", \"'.join(record_set.records) + "\"]")
    print("}")
    print("")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <aws_hosted_zone_id> ...")
        sys.exit(1)

    conn = route53.connect(
            aws_access_key_id='<SOME_ACCESS_KEY>',
            aws_secret_access_key='<THE_SECRET>'
    )

    match_id = ''.join(sys.argv[1:])
    print("/* Creating Zone: " + match_id + " */")
    zone = conn.get_hosted_zone_by_id(match_id)
    print("resource \"aws_route53_zone\" \"" + zone.name.replace(".", "_")[:-1] + "\" {")
    print("    name = \"" + zone.name[:-1] + "\"")
    print("}")
    print("")

    num_records = 0
    for record_set in zone.record_sets:
        num_records += 1
        if record_set.rrset_type == "A":
            if record_set.is_alias_record_set():
                alias_record(record_set)
            else:
                a_record(record_set)
        if record_set.rrset_type == "TXT":
            txt_record(record_set)
        if record_set.rrset_type == "MX":
            mx_record(record_set)
        if record_set.rrset_type == "CNAME":
            cname_record(record_set)
        if record_set.rrset_type == "NS":
            ns_record(record_set)

    print("/* DNS Records: " + str(num_records) + " */")
