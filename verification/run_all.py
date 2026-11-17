"""Run the scientific checks; optional reports go outside this source tree."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

CHECKS = ['check_finite_budget.py','check_calibration.py',
          'check_implementation.py','check_global_bounds.py','check_receiver.py']


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    if args.output_dir:
        out=args.output_dir.resolve()
        if out.is_relative_to(here.parent):
            parser.error('choose an output directory outside the source repository')
        out.mkdir(parents=True,exist_ok=True)
    passed=[]
    for check in CHECKS:
        result=subprocess.run([sys.executable,str(here/check)],text=True,capture_output=True)
        if args.output_dir:
            (out/(Path(check).stem+'.txt')).write_text(result.stdout+result.stderr)
        if result.returncode:
            print(result.stdout);print(result.stderr,file=sys.stderr)
            raise SystemExit(result.returncode)
        passed.append(check)
        print('PASS:',check,flush=True)
    report={'status':'passed','checks':passed,
       'scope':'Exact rational certificates and selected numerical identities; see verification/README.md.'}
    if args.output_dir:(out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
