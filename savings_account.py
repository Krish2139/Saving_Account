from pyteal import *

def savings_account(lock_period: int):
    start_time = Global.latest_timestamp()
    deadline = start_time + Int(lock_period)

    is_withdrawal = Txn.application_args[0] == Bytes("withdraw")

    can_withdraw = And(
        Global.latest_timestamp() >= deadline,
        Txn.sender() == Global.creator_address()
    )

    program = Cond(
        [Txn.application_id() == Int(0), Approve()],
        [is_withdrawal, If(can_withdraw, Approve(), Reject())],
        [Int(1), Reject()]
    )

    return program

if __name__ == "__main__":
    lock_period_seconds = 60 * 60 * 24 * 30
    approval_program = compileTeal(savings_account(lock_period_seconds), mode=Mode.Application, version=5)
    clear_program = compileTeal(Approve(), mode=Mode.Application, version=5)

    with open("approval.teal", "w") as f:
        f.write(approval_program)

    with open("clear.teal", "w") as f:
        f.write(clear_program)