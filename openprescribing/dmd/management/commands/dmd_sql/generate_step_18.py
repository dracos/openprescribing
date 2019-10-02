field_names = [
    "dmdid",
    "bnf_code",
    "vpid",
    "name",
    "full_name",
    "ema",
    "pres_statcd",
    "avail_restrictcd",
    "product_type",
    "non_availcd",
    "concept_class",
    "nurse_f",
    "dent_f",
    "prod_order_no",
    "sched_1",
    "sched_2",
    "padm",
    "fp10_mda",
    "acbs",
    "assort_flav",
    "catcd",
    "tariff_category",
    "flag_imported",
    "flag_broken_bulk",
    "flag_non_bioequivalence",
    "flag_special_containers",
]

print("-- Generated by generate_step_18.py")
print()
print("INSERT INTO dmd_product(")
for fn in field_names[:-1]:
    print("  {},".format(fn))
print("  {}".format(field_names[-1]))
print(")")
print("SELECT")
for fn in field_names[:-1]:
    print("  {},".format(fn))
print("  {}".format(field_names[-1]))
print("FROM dmd_product_temp")
print("ON CONFLICT (dmdid) DO UPDATE SET")
for fn in field_names[:-1]:
    print("  {} = EXCLUDED.{},".format(fn, fn))
print("  {} = EXCLUDED.{}".format(field_names[-1], field_names[-1]))
print(";")
