import unittest
from unittest.mock import patch

import main


class PomoTests(unittest.TestCase):
    def test_format_mm_ss(self):
        self.assertEqual(main.format_mm_ss(0), "00:00")
        self.assertEqual(main.format_mm_ss(61), "01:01")
        self.assertEqual(main.format_mm_ss(-5), "00:00")

    @patch("main.notify")
    @patch("main.countdown")
    def test_work_session_runs_work_and_break(self, countdown, notify):
        main.run_work_then_break(25, 5)

        self.assertEqual(countdown.call_args_list[0].args, ("Lock in", 25))
        self.assertEqual(countdown.call_args_list[1].args, ("Break", 5))
        self.assertEqual(notify.call_count, 2)

    @patch("main.subprocess.run")
    @patch("main.subprocess.Popen")
    def test_notify_is_noop_outside_macos(self, popen, run):
        with patch("main.sys.platform", "linux"):
            main.notify("Done")

        popen.assert_not_called()
        run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
