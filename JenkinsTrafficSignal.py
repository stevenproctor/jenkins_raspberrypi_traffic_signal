import argparse
import time

from JenkinsStatus import JenkinsStatus
from TrafficSignal import TrafficSignal


def __get_parsed_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--green-pin', dest='green_pin', action='store',
                       type=int, required=True,
                       help='Pin on the Raspberry Pi to control the green light')
    parser.add_argument('--yellow-pin', dest='yellow_pin', action='store',
                       type=int, required=True,
                       help='Pin on the Raspberry Pi to control the yellow light')
    parser.add_argument('--red-pin', dest='red_pin', action='store',
                       type=int, required=True,
                       help='Pin on the Raspberry Pi to control the red light')
    parser.add_argument('--jenkins-server', dest='jenkins_host', action='store',
                       required=True,
                       help='Jenkins hostname')
    parser.add_argument('--jenkins-port', dest='jenkins_port', action='store',
                       type=int, default=80,
                       help='Port the Jenkins host runs on')
    parser.add_argument('--jenkins-project', dest='jenkins_project', action='store',
                       required=True,
                       help='Project name to check Jekins for')
    parser.add_argument('--check_interval', dest='check_interval', action='store',
                       type=int, default=30,
                       help='How often to check the status of the Jenkins project')
    return parser.parse_args()


def run_signal(traffic_signal, status_checker, check_interval):
    while True:
        status = status_checker.get_status()
        __status_codes_to_traffic_command[status](traffic_signal)
        time.sleep(check_interval)

def __build_passed(traffic_signal):
    traffic_signal.reset()
    traffic_signal.on(traffic_signal.green)

def __build_failed(traffic_signal):
    traffic_signal.reset()
    traffic_signal.on(traffic_signal.red)

def __build_unknown(traffic_signal):
    traffic_signal.reset()
    traffic_signal.on(traffic_signal.yellow)

def __build_unavailable(traffic_signal):
    traffic_signal.reset()


__status_codes_to_traffic_command = {
    "SUCCESS" : __build_passed,
    "FAILURE" : __build_failed,
    "UNKNOWN" : __build_unknown,
    "UNAVAILABLE" : __build_unavailable
}


def main():
    args = __get_parsed_args()
    status_checker = JenkinsStatus(args.jenkins_host, args.jenkins_port, args.jenkins_project)
    traffic_signal = TrafficSignal(green_pin=args.green_pin, yellow_pin=args.yellow_pin, red_pin=args.red_pin)
    try:
        run_signal(traffic_signal, status_checker, args.check_interval)
    finally:
	traffic_signal.reset()
        traffic_signal.close()

if __name__ == "__main__":
    # execute only if run as a script
        main()

