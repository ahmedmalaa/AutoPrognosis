'''
Test script that calls all test routines and notebooks in this directory
'''
import sys
import os
import argparse
from pathlib import Path


def init_sys_path():
    import os
    import sys
    proj_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir))
    sys.path.append(os.path.join(proj_dir, 'init'))
    import initpath
    initpath.platform_init_path(proj_dir)

init_sys_path()
import utilmlab    
    

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exe', help='python interpreter to use')
    parser.add_argument('--projdir')
    # parser.add_argument('--verbose', type=int, default=0)
    parser.add_argument('--it', type=int)
    parser.add_argument('--onlynotebook', type=int, default=0)
    return parser.parse_args()


if __name__ == '__main__':

    args = init_arg()

    is_only_notebook = args.onlynotebook

    if args.exe is not None:
        python_exe = args.exe
    else:
        python_exe = 'python' if sys.version_info[0] < 3 else 'python3'

    proj_dir = utilmlab.get_proj_dir() \
        if args.projdir is None else args.projdir

    logger = utilmlab.init_logger(
            '.', 
            'log_test_alg_{}.txt'.format(utilmlab.get_hostname()))

    if not is_only_notebook:

        # execute all unit tests

        f_lst = utilmlab.find_file_dir(
            '{}/alg'.format(proj_dir),
            'test_*.py')

        logger.info('Unit tests found:{}'.format(f_lst))

        for fpy in f_lst:
            if 'test_alg.py' in fpy:
                continue
            utilmlab.exe_cmd(
                logger,
                '{} {} {} {}'.format(
                    python_exe,
                    Path(fpy),
                    '--it {}'.format(args.it) if args.it is not None else '',
                    '--exe {}'.format(args.exe) if args.exe is not None else ''
                )
            )

    # execute all notebooks

    f_lst = utilmlab.find_file_dir(
        '{}/alg'.format(utilmlab.get_proj_dir()),
        '*.ipynb')

    logger.info('notebooks found:{}'.format(f_lst))

    cwd = os.getcwd()

    for fnb in f_lst:
        script = Path(fnb)

        utilmlab.exe_cmd(
            logger,
            'jupyter nbconvert {} --to python'.format(fnb))

        fpy = fnb.replace('.ipynb', '.py')
        os.chdir(os.path.dirname(fpy))
        utilmlab.exe_cmd(
            logger,
            '{} {} '.format(
                'ipython3',
                fpy))
        os.chdir(cwd)
        
    logger.info('-*-')
