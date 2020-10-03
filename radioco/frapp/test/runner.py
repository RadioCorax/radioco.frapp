import os
import sys


os.environ['DJANGO_SETTINGS_MODULE'] = 'radioco.frapp.test.settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


def runtests(*test_labels):
    from django_nose import NoseTestSuiteRunner

    runner = NoseTestSuiteRunner(verbosity=1, interactive=True)
    failures = runner.run_tests(test_labels)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
