import cash_on_hand, profit_loss, overheads

def main():
    """
    - Main function which coordinates and executes the functions FindMaxOverhead, CashOnHand and ProfitLoss
    """
    overheads.FindMaxOverhead()
    cash_on_hand.CashOnHand()
    profit_loss.ProfitLoss()

main()