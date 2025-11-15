# 🧠 Marvellous Process Logger

A Python automation script that scans all running system processes and logs their details into timestamped files every 6 minutes. Built for system monitoring, auditing, and learning process management using Python.

---

## 📌 Features

- Scans all active processes on the system
- Captures:
  - Process ID (PID)
  - Process name
  - Username
  - Virtual memory usage (in MB)
- Logs are saved in a folder named `MarvelllousProcessX`
- Each log file is timestamped for easy tracking
- Runs automatically every 6 minutes using the `schedule` module

---

## 🛠 Requirements

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)
- [schedule](https://pypi.org/project/schedule/)

Install dependencies:

```bash
pip install psutil schedule
