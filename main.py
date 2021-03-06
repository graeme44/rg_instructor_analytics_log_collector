"""
Enterpoint.
"""
import argparse

import django

from rg_instructor_analytics_log_collector.raw_log_loaders import run_ziped_file_loader
from rg_instructor_analytics_log_collector.repository import MySQlRepository


def main():
    """
    Start app.
    """
    parser = argparse.ArgumentParser(
        description='App for load logs records in to mysql'
    )
    parser.add_argument(
        '--tracking_log_dir',
        action="store",
        dest="tracking_log_dir",
        type=str,
        default='/edx/var/log/tracking'
    )
    arg = parser.parse_args()
    django.setup()

    repository = MySQlRepository()
    run_ziped_file_loader(arg.tracking_log_dir, repository)


if __name__ == "__main__":
    main()
