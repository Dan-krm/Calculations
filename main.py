# Author: Dan Richmond-Martina
# A program that calculates different things like the amount of debt that needs to be paid,
# profit share from the proceeds of a sale, a speed calculation and a travel expense calculation.
import debt
import profitShare
import speed
import tripCost


if __name__ == '__main__':
    debt.debt_payment()
    profitShare.profit_share()
    speed.display_speed()
    tripCost.display_trip_cost()
