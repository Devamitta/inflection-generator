#!/usr/bin/env python3

import argparse

from rich import print  # pylint: disable=redefined-builtin

import modules

from helpers import Kind, timeis


def _get_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=[i.name for i in Kind])
    parser.add_argument("--class-file-name", type=str, default='1')
    return parser


def main(args: argparse.Namespace):
    print(f"{timeis()} ----------------------------------------")

    inflection_table_index = modules.create_inflection_table_index()
    inflection_table = modules.create_inflection_table_df()

    modules.test_inflection_pattern_changed(inflection_table_index, inflection_table)

    kind = Kind[args.kind]

    if kind == Kind.DPS:
        modules.create_dps_df()
    elif kind == Kind.SBS:
        modules.create_sbs_df(args.class_file_name)

    modules.test_for_missing_stem_and_pattern()
    modules.test_for_wrong_patterns(inflection_table_index)
    modules.test_for_differences_in_stem_and_pattern()
    modules.test_if_inflections_exist_dps()
    modules.test_if_inflections_exist_suttas()  # nu
    modules.generate_changed_inflected_forms()
    modules.combine_old_and_new_dataframes()
    modules.generate_html_inflection_table(kind)
    modules.generate_inflections_in_table_list()
    modules.transcribe_new_inflections()
    modules.combine_old_and_new_translit_dataframes()
    modules.export_translit_to_pickle()
    modules.export_inflections_to_pickle()
    modules.delete_unused_inflection_patterns(inflection_table_index)
    modules.delete_old_pickle_files()
    modules.delete_unused_html_tables()
    modules.delete_unused_inflections()
    modules.delete_unused_inflections_translit()

    print(f"{timeis()} ----------------------------------------")


if __name__ == "__main__":
    ARGS = _get_argparser().parse_args()
    main(ARGS)
