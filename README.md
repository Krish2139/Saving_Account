# Savings Account Smart Contract (PyTeal)

## Overview

This PyTeal smart contract implements a Savings Account on Algorand that locks funds for a fixed period. Withdrawals are only allowed after the lock period ends and only by the creator of the contract.

## Features

- Lock funds for a specified time period (default 30 days)
- Only the creator can withdraw funds
- Withdrawal allowed only after the lock period has passed

## Files

- `savings_account.py` — PyTeal source code that generates approval and clear state TEAL programs.
- `approval.teal` — Compiled approval program.
- `clear.teal` — Compiled clear state program.

## Usage

1. Compile the smart contract by running:
    ```bash
    python3 savings_account.py
    ```

2. Deploy the generated `approval.teal` and `clear.teal` on the Algorand blockchain.

3. To withdraw funds, submit an application call transaction with the argument `"withdraw"` **after** the lock period.

## Parameters

- Lock period is set in seconds in the script (`lock_period_seconds`), default is 30 days (2,592,000 seconds).

## Requirements

- Python 3.x
- PyTeal package (`pip install pyteal`)
- Algorand SDK for deployment (optional, for contract deployment and interaction)

## License

MIT License