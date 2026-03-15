# 204-project-overview-and-solution-architecture.md



## Setup

We will be simulating on a real-time streaming scenario.

More specifically,
we are going to simulate a system for monitoring the structural health of bridges.

- each of 5 major European bridges has been equipped with 3 IoT sensors

- each sensor takes a reading of a particular structural-health metric every minute,
  and
  streams the taken reading

- the sensors/metrics are

  - ambient temperature
  
  - deck vibration
  
  - tilt angle



## Objective

Enable operators to detect unusual spikes or creeping lean in near-real-time

In other words:
Implement a pipeline, which
processes the sensors' readings - which are data streams! -
by continuously aggregating and correlating those readings
