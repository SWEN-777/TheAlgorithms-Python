# Security Testing Instructions

## Setup
Activate your virtual environment and install Bandit:
```bash
pip install bandit
```

## Run Security Tests
Run Bandit across multiple folders:
```bash
bandit -r <Directory>
```

## Expected Output
- Bandit: Reports on insecure coding patterns (e.g., use of assert, weak randomness).