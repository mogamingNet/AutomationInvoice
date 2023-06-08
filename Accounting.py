#!/usr/bin/python3

#JOURNAL ENTRY


invoice = True



while invoice:
	
		sales = int(input('\33[33m'"how much sales did you collected\n"))

		tax = 0.14

		sales_tax = sales * tax


		Total_sales = sales + sales_tax

		print (f"Cash is debit {Total_sales}")

		print (f"sales is credit {sales}")

		print (f"salestax is credit {sales_tax}")  

		print ("------------------------Purchases--------")

		purchases = int(input('\33[34m'"how much purchases did you paid\n"))

		purchase_tax = purchases * tax

		Total_purchase = purchases + purchase_tax

		print (f"purchase is debit {purchases}")

		print (f"purchasetax is debit {purchase_tax}")

		print (f"cash is credit {Total_purchase}")


		nettax = sales_tax - purchase_tax
		print (f"the tax is {nettax}")

		if sales_tax == purchase_tax:
			print ("WOW you dont have tax ")

		else:
			print ("you have tax")		

		invoice += 1

		print ('\33[32m'f"the next invoice number {invoice} \n")

		if invoice > 5:
			print ("the invoices exceed 5 ")
			

		elif invoice == 100:
			print ("you exceed all invoices its full")
			exit()
		
		
