from flask import render_template, redirect, url_for, flash,request
from forms import ContactUsForm,DonateForm,PartnerForm
from models import ContactUs,Donate,Partner
from __init__ import  db, app


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


#success page

# routes for index,register,login,logout,error...

@app.route('/' ,methods=['GET','POST'])
    
def contact():    
    forms = ContactUsForm()
    if forms.validate_on_submit():        
        contactus = ContactUs(name=forms.name.data,
                    email=forms.email.data, address=forms.address.data,phone=forms.phone.data,comments=forms.comments.data)
        db.session.add(contactus)
        db.session.commit()
        #flash('hurreey account created','success')
        #return redirect(url_for('home'))
        #return redirect('contact')

    return render_template('index.html', forms=forms)

@app.route('/Donate_Food' ,methods=['GET','POST'])

def donate():
		#driver = webdriver.Chrome()
		products=[] #List to store name of the product
		prices=[] #List to store price of the product
		ratings=[] #List to store rating of the product
		driver.get("https://www.flipkart.com/search?q=nokia+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=RECENT&suggestionId=nokia+mobiles%7CMobiles&requestId=34c5d1f7-8967-44ef-82e4-d7d691ad0f72&as-backfill=on")

		content = driver.page_source
		soup = BeautifulSoup(content)
		for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
			name=a.find('div', attrs={'class':'_3wU53n'})
			price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
			rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
			products.append(name.text)
			prices.append(price.text)
    		#ratings.append(rating.text)

		df = pd.DataFrame({'Product Name':products,'Price':prices})
		df.to_csv('products.csv', index=False, encoding='utf-8')
		return "Success"

    
"""def donate():    
    forms = DonateForm()
    if forms.validate_on_submit():        
        donatefood = Donate(name=forms.name.data,
                    email=forms.email.data, address=forms.address.data,phone=forms.phone.data,food=forms.food.data)
        db.session.add(donatefood)
        db.session.commit()
        #flash('hurreey account created','success')
        

    return render_template('donate_food.html', forms=forms)"""

@app.route('/Partner' ,methods=['GET','POST'])
    
def partner():    
    forms = PartnerForm()
    if forms.validate_on_submit():        
        partner = Partner(orgname=forms.orgname.data,ownername=forms.ownername.data,
                    email=forms.email.data, phone=forms.phone.data,state=forms.state.data,city=forms.city.data,address=forms.address.data)
        db.session.add(partner)
        db.session.commit()
        

        import smtplib

        from string import Template

        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        MY_ADDRESS = 'your_mail_id'
        PASSWORD = 'your_password'

       
        def get_contacts(filename):
            """
            Return two lists names, emails containing names and email addresses
            read from a file specified by filename.
            """
            
            names = []
            emails = []
            with open(filename, mode='r', encoding='utf-8') as contacts_file:
                for a_contact in contacts_file:
                    names.append(a_contact.split()[0])
                    emails.append(a_contact.split()[1])
            return names, emails

        def read_template(filename):
            """
            Returns a Template object comprising the contents of the 
            file specified by filename.
            """
            
            with open(filename, 'r', encoding='utf-8') as template_file:
                template_file_content = template_file.read()
            return Template(template_file_content)

        def main():
            names, emails = get_contacts('mycontact.txt') # read contacts
            message_template = read_template('message.txt')

            # set up the SMTP server
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login(MY_ADDRESS, PASSWORD)

            # For each contact, send the email:
            for name, email in zip(names, emails):
                msg = MIMEMultipart()       # create a message

                # add in the actual person name to the message template
                message = message_template.substitute(PERSON_NAME=name.title())

                # Prints out the message body for our sake
                print(message)

                # setup the parameters of the message
                msg['From']=MY_ADDRESS
                msg['To']=email
                msg['Subject']="Thanks For Joining"
                
                # add in the message body
                msg.attach(MIMEText(message, 'plain'))
                
                # send the message via the server set up earlier.
                s.send_message(msg)
                del msg
                
            # Terminate the SMTP session and close the connection
            s.quit()
        main()
            

    


        

    return render_template('partner.html', forms=forms)

@app.route('/error')
def error():
    return render_template('error.html')
