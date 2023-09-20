import argparse
import re
from collections import defaultdict

# Regular expression to match log lines with charm name and severity
log_line_pattern = r'(?P<charm>.*?): (?P<timestamp>.*?) (?P<severity>INFO|DEBUG|WARNING|ERROR) (?P<message>.*)'

def parse_log_file(filename, charm_name=None):
    charms_warnings = defaultdict(list)
    severity_count = defaultdict(int)
    duplicate_messages = defaultdict(int)
    log_messages = defaultdict(int)
    total_messages = 0

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(log_line_pattern, line)
            if match:
                log_charm = match.group('charm')
                log_severity = match.group('severity')
                log_message = match.group('message')

                # If a charm_name is provided and it doesn't match, skip this log line
                if charm_name and log_charm != charm_name:
                    continue

                total_messages += 1
                log_messages[log_charm] += 1
                severity_count[log_severity] += 1

                # Track duplicate log messages
                message_key = f"{log_severity}:{log_message}"
                duplicate_messages[message_key] += 1

                # Collect warnings for each charm
                if log_severity == 'WARNING':
                    charms_warnings[log_charm].append(log_message)

    return charms_warnings, severity_count, duplicate_messages, log_messages, total_messages

def print_results(charms_warnings, severity_count, duplicate_messages, log_messages, total_messages):
    print("Warnings per charm:")
    for charm, warnings in charms_warnings.items():
        print(f"- {charm}:")
        for warning in warnings:
            print(f"  - {warning}")

    print("\nNumber of each severity of message:")
    for severity, count in severity_count.items():
        print(f"- {severity}: {count}")

    print("\nNumber of duplicate messages (and their severity):")
    for message, count in duplicate_messages.items():
        severity, message_text = message.split(':', 1)
        print(f"- Severity: {severity}, Message: {message_text}, Count: {count}")

    print("\nProportions of each type of log message for each charm:")
    for charm, charm_messages in log_messages.items():
        print(f"- {charm}:")
        for severity, count in severity_count.items():
            proportion = charm_messages / total_messages if total_messages > 0 else 0
            print(f"  - {severity}: {count} ({proportion:.2%})")

    print("\nTotal number of log messages per charm:")
    for charm, charm_messages in log_messages.items():
        print(f"- {charm}: {charm_messages}")

    print(f"\nTotal number of log messages: {total_messages}")

def main():
    parser = argparse.ArgumentParser(description="Juju Log Analyzer")
    parser.add_argument("filename", type=str, help="Path to the log file")
    parser.add_argument("--charm", type=str, help="Charm name (optional)")
    args = parser.parse_args()

    charms_warnings, severity_count, duplicate_messages, log_messages, total_messages = parse_log_file(args.filename, args.charm)
    print_results(charms_warnings, severity_count, duplicate_messages, log_messages, total_messages)

if __name__ == "__main__":
    main()
