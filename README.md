# dns-import-aws-to-tf

## get-route53-zone.py
Gets all records in a aws route53 hosted zone and imorts each one of them, as well as the zone itself, into a terraform state.

Takes the zone_id as parameter and writes the terraform code to stdout.

Usage: get-route53-zone.py <aws_zone_id> > some_file.tf

## imports.py
Writes all the import statements needed to import each record into the terraform state.

Takes the zone_id as parameter and writes the terraform cli import statements to stdout.

Usage: imports.py <aws_zone_id> > imports_statements.txt

## execute_imports.sh
Finally execute such imports into the terraform state.

Takes the import_statements.txt file and reads line by line, executing the terraform commands
