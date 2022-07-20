#!/usr/bin/env python3
# coding: utf-8 

from modules import *

def inflection_generator_for_dps():
	create_inflection_table_index()
	create_inflection_table_df()
	test_inflection_pattern_changed()
	create_sbs_df()
	test_for_missing_stem_and_pattern()
	test_for_wrong_patterns()
	test_for_differences_in_stem_and_pattern()
	test_if_inflections_exist_dps()
	test_if_inflections_exist_suttas() #nu
	generate_changed_inflected_forms()
	combine_old_and_new_dataframes()
	generate_html_inflection_table()
	generate_inflections_in_table_list()
	transcribe_new_inflections()
	combine_old_and_new_translit_dataframes()
	export_translit_to_pickle()
	export_inflections_to_pickle()
	delete_unused_inflection_patterns()
	delete_old_pickle_files()
	delete_unused_html_tables()
	delete_unused_inflections()
	delete_unused_inflections_translit()
	print(f"{timeis()} ----------------------------------------")


if __name__ == "__main__":
   inflection_generator_for_dps()