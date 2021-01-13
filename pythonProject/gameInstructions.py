def game_instructions():
    moneyBank = ["1,000,000", "500,000", "250,000","125,000","64,000","32,000","16,000","8,000","4,000","2,000","1,000","500","300","200","100"]

    print("""
    
    You will be asked 15 questions. The money value grows from $500 all the wayup to $1 MILLION. 
    
    Every question correctly answered moved you one step closer to that top prize. Remember you can always walk away with that money you have earned up to that point.
    
    An incorrect answer and you walk away with nothing until you get to those two thresholds - $1,000 then again at $32,000. """)
    time.sleep(5)
    for i in moneyBank:
        print("\n$"+i)

    time.sleep(1)
    print( """\n You have two lifelines:
    One, you can either choose to swap questions which will allow you to  discard the current question and receive a new question. You can type "swap" anytime to use this lifeline!

    Second, you have 50:50 which is an option that takes away two incorrect answers""")
    time.sleep(2)
