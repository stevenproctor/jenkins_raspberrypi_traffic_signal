# jenkins_raspberrypi_traffic_signal

Code for a RaspberryPi to control a "Traffic Signal" based off the results of a specified Jenkins build


# Running the "Traffic Signal"

```
sudo python JenkinsTrafficSignal.py --green-pin=11 --yellow-pin=16 --red-pin=22 --jenkins-server=localhost --jenkins-port=8080 --jenkins-project=test
```

## Full listing of command line options

```
sudo python JenkinsTrafficSignal.py -h
usage: JenkinsTrafficSignal.py [-h] --green-pin GREEN_PIN --yellow-pin
                               YELLOW_PIN --red-pin RED_PIN --jenkins-server
                               JENKINS_HOST [--jenkins-port JENKINS_PORT]
                               --jenkins-project JENKINS_PROJECT
                               [--check_interval CHECK_INTERVAL]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  --green-pin GREEN_PIN
                        Pin on the Raspberry Pi to control the green light
  --yellow-pin YELLOW_PIN
                        Pin on the Raspberry Pi to control the yellow light
  --red-pin RED_PIN     Pin on the Raspberry Pi to control the red light
  --jenkins-server JENKINS_HOST
                        Jenkins hostname
  --jenkins-port JENKINS_PORT
                        Port the Jenkins host runs on
  --jenkins-project JENKINS_PROJECT
                        Project name to check Jekins for
  --check_interval CHECK_INTERVAL
                        How often to check the status of the Jenkins project
```
