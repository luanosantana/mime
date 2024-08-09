# Mime
---

Mime is an application that aims to simulate the behavior of a real application, without actually performing actions. The objective is to have an easy application to simulate real environments with signals that are emitted by applications, such as errors, requests, CPU or memory load, among others.

## 1. Application behaviors

Among the signals we have from applications we can categorize expected and unexpected behaviors. Among the expected behaviors, we can highlight request, provision of routes, connection to database, increase in CPU or memory load; and among unexpected errors, application crash, not responding to sigterm signals, among others.

> Item with checked box means it is already implemented

### 1.1 Expected behaviors

- [x] Default routes
    - Healthcheck (`/healcheck`)
    - Info (`/info`)
- [ ] Load increase
    - vCPU
    - RAM memory

### 1.2 Unexpected behaviors

- [ ] Does not respond to signal term
    - SIGTERM 15
    - SIGTERM 9