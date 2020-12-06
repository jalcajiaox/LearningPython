def email_list(domains):
	emails = []
	i=0


	for key in domains: 
		users=domains[key]
		for user in users:
			
			emails.append(user+"@"+key)
			


	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

