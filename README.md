# Juju Log Analyzer

This Python command-line tool is designed to analyze Juju debug log files. It provides the output with insights into log messages, including warnings, severity counts, duplicate messages, proportions of each message type, and total message counts. The tool also allows to filter logs by charm name.

---

## Assumptions

- The log file is accessible and has appropriate read permissions.
- Python 3 is installed on the system.

---

## How to Run

1. Ensure you have Python 3 installed on your system.

2. Download or clone this repository to your local machine.

3. Open a terminal and navigate to the directory containing the `juju_log_analyzer.py` script.

4. Run the script with the following command, replacing `<path_to_log_file>` with the actual path to your Juju debug log file and `<charm_name>` with a charm name to filter by:

   ```bash
   python juju_log_analyzer.py <path_to_log_file> --charm <charm_name>
   ```

   - `<path_to_log_file>`: The full path to your Juju debug log file.
   - `<charm_name>`: The charm name to filter logs by. If omitted, logs for all charms will be analyzed.

---

## Code Approach

**Main Components of the Code**

1. **Log Line Pattern**:
   
   The code starts by defining a pattern for parsing log lines. Log lines in Juju log files have a specific format, including a charm name, timestamp, severity level (INFO, DEBUG, WARNING, ERROR), and the log message itself. The script uses a regular expression pattern to extract these components from each log line.

2. **Parsing the Log File**:

   It then proceeds to read the specified log file line by line. For each line, it checks if it matches the log line pattern. If it does, it extracts the charm name, severity level, and log message. If a charm name filter is provided, it only processes log lines for that specific charm.

3. **Data Collection**:

   The code collects various types of data as it processes the log lines:

   - **Warnings per Charm**: It keeps track of warnings (logs with severity "WARNING") for each charm separately.
   
   - **Severity Counts**: It counts the number of log messages for each severity level (INFO, DEBUG, WARNING, ERROR).

   - **Duplicate Message Counts**: It identifies and counts duplicate log messages, including their severity levels.

   - **Log Message Counts per Charm**: It keeps track of the total number of log messages for each charm.

   - **Total Message Count**: It counts the total number of log messages, irrespective of charm.

4. **Displaying Results**:

   Once the log file is processed, the code displays the collected data in a structured format. This includes showing the warnings for each charm, the counts of different severity levels, the counts of duplicate messages, proportions of each message type, and the total message count.

---

## End Notes
This code is valuable for monitoring and troubleshooting Juju deployments, providing insights into log messages, and assisting in maintaining the health of cloud orchestration systems. For better production use, we can consider additional improvements such as error handling, unit testing, packaging, security measures, and integration with monitoring systems.
The whole project took me 5 hours of work which includes researching about Juju(first time working with this), log files, debugging, programming and testing.

