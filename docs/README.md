<p align="center">
  <img src="/docs/images/netora-logo.png">
</p>

<p align="center">
  <b>Quickly uncover details and geolocation for any IP address</b>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="#general-usage">Usage</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
</p>

<br><br>


<p align="center">
  <img src="/docs/images/demo.png">


---

## Installation

You can install Netora via pip or run it directly from the cloned repository.


### Cloning the repository

1. Clone the repository:
   ```bash
   git clone https://github.com/nativevoid/netora
   ```
2. Install the required dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```
3. Run Netora:
   ```bash
   $ cd netora
   $ python netora.py 111.111.111.111
   ```

### Installing via pip

1. Install the `netora` package:
   ```bash
   pip install netora

2. That's it! Now you can run it from anywhere:
   ```bash
   $ netora 111.111.111.111
   ```


## General usage

To search for only one IP address:
```bash
netora 123.123.123.123
```

To search for more than one IP address:
```bash
netora 55.55.55.55 66.66.66.66 77.77.77.77
```

&nbsp;
```console
netora --help
usage: netora [-h] [--version] [--folderoutput FOLDEROUTPUT] [--output OUTPUT] [--no-color]
              IP_ADDRESSES [IP_ADDRESSES ...]

Netora: Quickly uncover details and geolocation for any IP address (Version: 0.15.0)

positional arguments:
  IP_ADDRESSES          One or more IP addresses for looking up location and network information.

options:
  -h, --help            show this help message and exit
  --version             Display version information.
  --folderoutput, -fo FOLDEROUTPUT
                        Multiple IP addresses can be used, and the results will be saved in this folder.
  --output, -o OUTPUT   Only one IP address can be used, and the result will be saved to this file.
  --no-color            Don't color terminal output
```

<br>

## Feature Requests & Bug Reporting

Want to suggest a new feature? Open a request using our [Feature Request Template](../.github/ISSUE_TEMPLATE/feature-request.yaml).

Found a bug? Report it using our [Bug Report Template](../.github/ISSUE_TEMPLATE/bug-report.yaml).

<br>

## Disclaimer

This tool is for educational purposes only and is intended to help with IP lookups. Users are responsible for complying with applicable laws.

By using this tool, you accept all risks associated with its use. Nativevoid is not liable for any consequences resulting from using this tool.


