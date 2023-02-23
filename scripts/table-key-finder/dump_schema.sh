#!/bin/sh
# note: source .export_password for $PGPASSWORD
SCHEMA="public"
DB="glopad3"
USER="glopad3"
alias psql="/Applications/pgAdmin\ 4.app/Contents/SharedSupport/psql"
QUERY="SELECT conrelid::regclass AS table_name,
       conname AS primary_key,
       pg_get_constraintdef(oid)
FROM   pg_constraint
WHERE  contype = 'p'
AND    connamespace = 'public'::regnamespace
ORDER  BY conrelid::regclass::text, contype DESC;"
QUERY2="copy (select 'foo' as bar,* from d_digdoc where false) to STDOUT DELIMITER ',' CSV HEADER;"
QUERY3="copy (select table_name,* from d_digdoc,information_schema.tables where false) to STDOUT DELIMITER ',' CSV HEADER;"

# psql -U $USER -p 5438 -h 127.0.0.1 -Atc "$QUERY" $DB

# exit 0

psql -U $USER -p 5438 -h 127.0.0.1 -Atc "select tablename from pg_tables where schemaname='$SCHEMA'" $DB |\
  while read TBL; do
    psql -U $USER -p 5438 -h 127.0.0.1 -c "COPY (select 'x' AS $TBL,* from $TBL where false) TO STDOUT DELIMITER ',' CSV HEADER" $DB >> "output/tables.csv"
    # psql -U $USER -p 5438 -h 127.0.0.1 -c "COPY $SCHEMA.$TBL TO STDOUT" $DB > $TBL.csv
  done
