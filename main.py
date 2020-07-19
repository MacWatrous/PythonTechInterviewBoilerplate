#!/usr/bin/python3

from testcases import cases, expected_results
from test_timer import TestTimer, duration_to_string, avg_and_median_from_durations


def execute_test_case(case):
    return case


# Entry point which runs test cases and times them.
if __name__ == '__main__':
    execution_count = 1
    durations = []
    for case, expected_result in zip(cases, expected_results):
        timer = TestTimer()
        timer.start()
        result = execute_test_case(*case)
        timer.stop()
        case_duration = timer.get_microseconds()
        durations.append(case_duration)

        if result != expected_result:
            print("❌ Case ({}/{}) [{}]"
                  .format(execution_count, len(cases), duration_to_string(case_duration)))
            print(case)
            print("--------------------------------------")
        else:
            print("✔ Case ({}/{}) [{}]"
                  .format(execution_count, len(cases), duration_to_string(case_duration)))
        execution_count += 1
    average_time, median_time = avg_and_median_from_durations(durations)
    print("Average execution time:{}".format(duration_to_string(average_time)))
    print("Median execution time:{}".format(duration_to_string(median_time)))

