# Quick_Emergency_Chatting

## Overview

Quick_Emergency_Chatting is a command-line chatting application designed for emergency communication within a local network (LAN) using wireless EM waves. It operates without reliance on traditional internet or messaging services, making it ideal for use during power outages or network breakdowns.

## Features

- **Local Network Communication:** Utilizes socket programming to establish wireless communication within a specific communication range.
- **Anonymity:** Messages are sent anonymously to ensure user privacy.
- **Security:** Implements a level of security to protect messages during transmission.
- **Error Handling:** Includes error handling mechanisms to manage unexpected issues during communication.

## Usage

### Prerequisites

- Python 3.5 or higher installed on both the sender and receiver devices.

### Setup

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.

### Running the Application

#### Master Sender Setup

1. Open `server_chat.py` in a text editor.
2. Modify the IP address and port according to your network configuration. The master server_chat.py file will be the one sending messages and whose IP will be used for addressing and communication.
3. Run `server_chat.py`.
4. Enter your secret code after each message to authenticate.

#### Slave Receiver Setup

1. Open `client_chat.py` in a text editor.
2. Modify the IP address and port according to your network configuration.
3. Run `client_chat.py`. The slave receiver will be the one receiving messages.
4. Enter your secret code after each message to authenticate.

### Error Handling

- The application includes error handling mechanisms to manage connection issues, input validation, and unexpected errors during communication.
- Refer to the error messages displayed in the terminal for troubleshooting.

## Communication Method

- The communications will happen wirelessly through EM waves, without any hindrance or traffic, ensuring reliable communication during emergencies.

## User Interface

- The application is designed for a basic command line interface without the need for any GUI installation. 

## Notes

- This application is designed for use within a local network using wireless EM waves and does not require internet connectivity.
- Ensure that both the sender and receiver devices are within the specified communication range.
- Use secret codes after each message to authenticate and ensure secure communication.
- This application is intended for emergency communication and may not have the same features as traditional messaging applications.
