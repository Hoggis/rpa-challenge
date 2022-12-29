
class RpaChallenge:
    start_button = '//button[text()="Start"]'
    company_name = '//label[text()="Company Name"]/following-sibling::input'
    first_name = '//label[text()="First Name"]/following-sibling::input'
    last_name = '//label[text()="Last Name"]/following-sibling::input'
    role_in_company = '//label[text()="Role in Company"]/following-sibling::input'
    address = '//label[text()="Address"]/following-sibling::input'
    email = '//label[text()="Email"]/following-sibling::input'
    phone_number = '//label[text()="Phone Number"]/following-sibling::input'
    submit_button = '//input[@class="btn uiColorButton"]'
    result_text = '//div[@class="message2"]'
