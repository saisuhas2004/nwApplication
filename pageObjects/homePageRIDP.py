class homePageRIDP:
    # Home Page
    popup = "//img[contains(@src, 'svg-close-btn-white-1.svg')]"
    logIn = "//a[@class='hc-c-logged-out-links__link sl-c-login sl_swap']"
    loginTitle = "//title[contains(text(), 'HealthCare.gov')]"
    createAccount = "//a[text()='Create account']"

    # Create an account page
    pickTheStateYouLiveInDropDown = "//*[@id='dropdown--9__button-content']"
    pickTheState = "//*[@class='ds-c-dropdown__menu-container ds-c-field--medium']//li/span[text()='North Carolina']"
    firstName = "firstName"
    lastName = "lastName"
    emailAddress = "email"
    password = "Password"
    securityQuestionOneDropDown = "//*[@data-testid='securityQuestionOne']/span"
    securityQuestionOne = "//span[text()='What is your favorite radio station?']"
    securityQuestionOneAns = "answer1"
    securityQuestionTwoDropDown = "//*[@data-testid='securityQuestionTwo']"
    securityQuestionTwo = "//span[text()='What was your favorite toy when you were a child?']"
    securityQuestionTwoAns = "answer2"
    securityQuestionThreeDropDown = "//*[@data-testid='securityQuestionThree']"
    securityQuestionThree = "//span[text()='What is your favorite cuisine?']"
    securityQuestionThreeAns = "answer3"
    iUnderstandCheckBox = "terms-checkbox"
    createAccountButton = "create-account-button"
    accountCreationMessage = "//h2[text()='Verify your email address to finish creating your account']"

    # https://message-checker.appspot.com/
    emailAddressTextbox = "address"
    checkMessageButton = "//button[text()='Check for messages']"
    checkMailInBox = "//a[@id='subject-0']"
    verifyMyEmailAddress = "//a/img[@alt='verify my email address']"





    # login
    loginButton = "//*[@data-testid='loginButton']"
    username = "Username"
    password = "Password"
    login = "login-button"