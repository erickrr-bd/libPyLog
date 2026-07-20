# libPyLog (v2.2.1)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Logging Engine](https://img.shields.io/badge/engine-standard%20logging-orange.svg)](https://docs.python.org/3/library/logging.html)
[![Security Hardening](https://img.shields.io/badge/security-Pentest--compliant-brightgreen.svg)](#)

**libPyLog** is a dynamic, performance-optimized, and security-hardened logging utility written in Python. Specially designed for command-line applications (CLI/TUI), terminal environments, and system services, it acts as a robust wrapper on top of Python's native `logging` library.

It automates dual-stream output (terminal/file), daily file rotation, and strictly enforces UNIX-level security policies (such as owner assignments and restricted file permissions) to protect operational logs from unauthorized read access.

---

## ✨ Features

*   **Dual-Channel Output:** Simultaneously write logs to the terminal (`StreamHandler`) and physical files (`FileHandler`) dynamically, on the fly.
*   **Automated Daily Rotation:** Group and store files dynamically using daily-segmented names (`your-log-YYYY-MM-DD.log`).
*   **Smart Handler Management (Resource Leak Prevention):** Prevents the operating system from spawning duplicate file descriptors or leaking memory by caching and reusing active handlers rather than constantly purging them.
*   **Security Hardening (CWE Mitigations):** Restricts file access permissions to `640` (Read/Write for Owner, Read for Group, None for World) and optionally updates the OS-level user and group properties to comply with strict system-hardening policies.
*   **Granular Severity Mapping:** Offers an intuitive abstraction layer matching integer-based criticalities (1–5) to native Python logging levels (`DEBUG` to `CRITICAL`).

---

## 🛠️ Security Hardening (Pentest-Compliant)

Standard logging implementations often create files with generic system permissions (such as `644`), exposing potential technical errors, network paths, and structural layouts to unauthorized local users. 

**libPyLog** systematically mitigates this risk by:
1.  Enforcing restricted file permissions (`640`) upon creating a log file for the day.
2.  Assigning explicit low-privilege service ownership (e.g., `snap_tool:snap_tool`) using standard system utilities.
3.  Wrapping system ownership routines inside isolated exception boundaries to ensure that any local execution without administrative privileges (`sudo`) does not halt execution of the application's core logic.

---

## ⚙️ Requirements

To run this library and its integration modules, the following system and Python specifications are required:

### 1. System & Runtime Environment
* **Python 3.10+**: Crucial for native pattern matching syntax (`match-case`) used across the routing and logging engines.
* **Linux OS**: Required for managing native file ownership (`chown`), system groups, and execution permissions (`chmod`).

### 2. Python Dependencies
* **libPyUtils**

---

## 📋 API Usage Reference

### Method: `create_log`

```python
def create_log(self, message: str, level: int, name: str, **kwargs) -> None
```

Parameters:
- message (str): The text message or exception object to register.
- level (int): Logging severity represented as an integer:
    - 1: DEBUG
    - 2: INFO
    - 3: WARNING
    - 4: ERROR
    - 5: CRITICAL
- name (str): The unique identifier/logger channel name.

Keyword Arguments (kwargs):
- use_stream_handler (bool): If True, enables clean stdout logging format to the terminal.
- use_file_handler (bool): If True, enables writing logs to disk. (Requires file_name).
- file_name (str): Base file path/prefix where the date-bound file will be created.
- user (str): The target UNIX user who will own the file.
- group (str): The target UNIX group who will own the file.

---

## 🚀 Quick Start Example
Here is how you can seamlessly integrate libPyLog into your application:

```python
from libPyLog import libPyLog

# Initialize the logger
logger = libPyLog()

# 1. Standard Console-only Informational Log
logger.create_log(
    message="System menu rendered successfully.",
    level=2,  # INFO
    name="TUI_Menu",
    use_stream_handler=True
)

# 2. Hardened File-only Warning Log
# This will write to: "/var/log/snap-tool-2026-07-14.log"
logger.create_log(
    message="Connection attempt took longer than expected.",
    level=3,  # WARNING
    name="ES_Network",
    use_file_handler=True,
    file_name="/var/log/snap-tool",
    user="snap_tool",
    group="snap_tool"
)

# 3. Secure Error Log (Both Console & File Output)
try:
    1 / 0
except ZeroDivisionError as e:
    logger.create_log(
        message=f"Critical operation failed: {str(e)}",
        level=4,  # ERROR
        name="Calculator",
        use_stream_handler=True,
        use_file_handler=True,
        file_name="/var/log/snap-tool",
        user="snap_tool",
        group="snap_tool"
    )
```
---

## 📄 File Permissions Verification
Once the log file is generated, you can verify that the library successfully enforced system permissions and restricted local exposure:}

```bash
$ ls -l /var/log/snap-tool-*.log
-rw-r----- 1 snap_tool snap_tool 342 Jul 14 17:15 /var/log/snap-tool-2026-07-14.log
```
(Notice the -rw-r----- [640] mask, preventing standard local system users from accessing and viewing technical stack traces).
