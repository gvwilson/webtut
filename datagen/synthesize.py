"""Synthesize data."""

import argparse
import json
from pathlib import Path
import random
import sys

from grid import Grid
from parameters import Parameters
from person import Person
from sample import Sample
import utils


def main():
    """Main command-line driver."""
    args = _parse_args()

    if args.defaults:
        print(utils.json_dump(Parameters()))
        return 0
    elif not args.outdir:
        print("output directory not specified (use --outdir name)", file=sys.stderr)
        return 1

    params = _initialize(args)
    grids, persons, samples = _synthesize(params)
    _save(args, grids, persons, samples)

    return 0


def _initialize(args):
    """Initialize for data synthesis."""
    if args.params:
        with open(args.params, "r") as reader:
            params = Parameters.model_validate(json.load(reader))
    else:
        params = Parameters()

    random.seed(params.seed)

    return params


def _parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--defaults", action="store_true", help="show default parameters"
    )
    parser.add_argument("--outdir", default=None, help="output directory")
    parser.add_argument("--params", default=None, help="JSON parameter file")
    return parser.parse_args()


def _save(args, grids, persons, samples):
    """Save synthesized data."""
    outdir = Path(args.outdir)
    if not outdir.is_dir():
        outdir.mkdir(exist_ok=True)

    for g in grids:
        with open(outdir / f"{g.id}.csv", "w") as writer:
            print(g, file=writer)

    for name, cls, data in (("persons", Person, persons), ("samples", Sample, samples)):
        with open(outdir / f"{name}.csv", "w") as writer:
            print(cls.csv_header(), file=writer)
            for record in data:
                print(record, file=writer)


def _synthesize(params):
    """Synthesize data."""
    grids = [Grid.make(params) for _ in range(params.num_grids)]
    persons = [Person.make(params) for _ in range(params.num_persons)]
    samples = [Sample.make(params, grids, persons) for _ in range(params.num_samples)]
    return grids, persons, samples


if __name__ == "__main__":
    sys.exit(main())
