# Rasa Pro Setup & Deployment Guide

This documentation explains how to set up, run, and manage a Rasa Pro project locally and with Docker.

---

# Requirements

* Python `3.10` or `3.11`
* Docker
* Docker Compose
* Git

---

# Local Installation

## 1. Install Python

Make sure you are using:

* Python `3.10`
* or Python `3.11`

You can verify your version with:

```bash
python --version
```

---

## 2. Install Rasa Pro

Install Rasa Pro using pip:

```bash
pip install "rasa-pro"
```

---

## 3. Initialize a Rasa Project

Create a new Rasa project using the tutorial template:

```bash
rasa init --template tutorial
```

---

## 4. Train the Model

Train the assistant after making changes to the project:

```bash
rasa train
```

---

## 5. Run Rasa Inspector

Start the Rasa Inspector UI:

```bash
rasa inspect
```

---

# Git Workflow

## Clone Repository

Clone the project from GitHub:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/username/project-name.git
```

---

## Pull Latest Changes

Update your local project with the latest changes from GitHub:

```bash
git pull
```

---

# Docker Setup

## Install Docker

Download and install Docker:

* Docker Desktop (Windows/Mac)
* Docker Engine (Linux)

Official website:

[Docker](https://www.docker.com/?utm_source=chatgpt.com)

---

## Start the Containers

Run the project using Docker Compose:

```bash
docker compose up
```

To run in detached mode:

```bash
docker compose up -d
```

---

# Default Ports

The Docker containers use the following ports:

| Service        | Port   |
| -------------- | ------ |
| Rasa Assistant | `5005` |
| Action Server  | `5055` |
| Rasa Inspector | `5006` |

---

# Stop the Containers

Stop and remove all running containers:

```bash
docker compose down
```

This command will:

* Stop all containers
* Remove containers created by Docker Compose
* Keep project files intact

---

# Common Commands

## Train the Assistant

```bash
rasa train
```

## Start Rasa Server

```bash
rasa run
```

## Start Action Server

```bash
rasa run actions
```

## Open Inspector

```bash
rasa inspect
```

---

# Notes

* Use Python `3.10` or `3.11` for best compatibility with Rasa Pro.
* Re-train the model after updating intents, stories, rules, or domain files.
* Docker is recommended for easier deployment and environment consistency.
