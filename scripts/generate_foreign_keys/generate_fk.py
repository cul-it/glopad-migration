from typing import List
import csv


# Input is one or more primary keys inside parenthesis
# E.g. PRIMARY KEY (aaa [, bbb, etc])
# Output is a list of strings
# Output: ["aaa", ...]
def get_pk(pk_field: str) -> List[str]:
    pks = pk_field.split("PRIMARY KEY (")[1]
    pks = pks.split(")")[0]
    return pks.split(", ")


# table -> primary key map
table_to_pk = {}

# primary -> table map for unique values, only
# E.g. If only table a has primary key named "pk_a", it will be here.
# Otherwise, if table b and c share same name "pk_bc", it will not be here.
unique_pk_to_table = {}

# On this iteration, loop for non relation tables and populate all the
# primary key mapping.
with open("glopad_primary.txt") as gp:
    gp_reader = csv.reader(gp, delimiter="|")
    for gp_table in gp_reader:
        pks = get_pk(gp_table[2])
        if len(pks) == 1 and not gp_table[0].endswith("_ml"):
            table_to_pk[gp_table[0]] = pks[0]
            if pks[0] in unique_pk_to_table:
                unique_pk_to_table[pks[0]] = None

            else:
                unique_pk_to_table[pks[0]] = gp_table[0]

shared_pk_name_exceptions = {
    "r_pa_artsofperformance,artsofperformanceid": "d_production",
    "r_pa_group_geographic_aff,affid": "d_place_affiliation",
    "r_person_country,countryid": "d_country",
    "r_place_country,countryid": "d_country",
}
unrecognized_pk_name_exceptions = {
    "r_person_culturalid,culturalid": "d_culture",
    "r_person_group,groupid": "d_person_group",
    "r_piece,relatedpieceid": "d_piece",
    "r_production,relatedproductionid": "d_production",
}
# In this iteration, loop through all the relation tables
# and generate foreign key sql statements.
def get_fk_sql(tbl_name: str, fk_column: str) -> str:
    reference_tbl_name = unique_pk_to_table.get(fk_column)
    if not reference_tbl_name:
        # Multiple tables share this primary key name.
        # Deduce reference table name from the source.
        if tbl_name.endswith("_ml"):
            reference_tbl_name = tbl_name.split("_ml")[0]
        elif fk_column in unique_pk_to_table:
            # key exists but not unique
            if tbl_name.startswith("r_"):
                d_tbl_name = "d_" + tbl_name.split("r_")[1]
                if d_tbl_name in table_to_pk:
                    # it is a valid d_ table
                    reference_tbl_name = d_tbl_name
                else:
                    reference_tbl_name = shared_pk_name_exceptions.get(
                        f"{tbl_name},{fk_column}"
                    )
                    if not reference_tbl_name:
                        print(f"IDK: {tbl_name} -> {fk_column}")
                        return ""
            else:
                print(f"IDK: {tbl_name} -> {fk_column}")
                return ""
        else:
            reference_tbl_name = unrecognized_pk_name_exceptions.get(
                f"{tbl_name},{fk_column}"
            )
            if not reference_tbl_name:
                # Primary key not found
                print(f"{tbl_name} -> {fk_column}")
                return "I"

    constraint_name = f"{tbl_name}_{reference_tbl_name}_{fk_column}"
    sql = (
        f"ALTER TABLE {tbl_name} "
        f"ADD CONSTRAINT {constraint_name} "
        f"FOREIGN KEY ({fk_column}) "
        f"REFERENCES {reference_tbl_name} ({table_to_pk[reference_tbl_name]});"
    )
    return sql


sqls = []
with open("glopad_primary.txt") as gp:
    gp_reader = csv.reader(gp, delimiter="|")
    for gp_table in gp_reader:
        if gp_table[0].startswith("pg_") or gp_table[0].startswith("f_"):
            continue
        pks = get_pk(gp_table[2])
        if len(pks) > 1 or gp_table[0].endswith("_ml"):
            for fk in get_pk(gp_table[2]):
                sql = get_fk_sql(gp_table[0], fk)
                if sql and sql != "I":
                    sqls.append(sql)

for sql in sqls:
    print(sql)
