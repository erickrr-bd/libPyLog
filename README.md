# libPyLog (2.2.1)

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

## 📋 API Usage Reference

### Method: `create_log`

```python
def create_log(self, message: str, level: int, name: str, **kwargs) -> None
