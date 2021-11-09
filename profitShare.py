# Author: Dan Richmond-Martina

def profit_share():
    print("\n2: Profit Share\n")
    payment = float(input("Enter the amount of payment received: "))
    workers = float(input("Enter the number of people you are distributing the profits to: "))
    manager_margin = (0.25 * payment)
    worker_margin = (0.75 * payment)
    distributed_total = ((0.75 * payment)/workers)
    print("The managers 25% share of the payment received is worth: $" + str(manager_margin))
    print("The workers 75% share of the payment for the case is worth: $" + str(worker_margin))
    print("Each worker that is not the manager takes home: $" + str(distributed_total), "for their efforts.")
