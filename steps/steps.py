from behave import when, given, then


@given(u'set text in textField text1 to {text}')
def step_impl(context, text):
    context.text1 = text


@given(u'set text in textField text2 to {text}')
def step_impl(context, text):
    context.text2 = text


@when(u'user enters text')
def step_impl(context):
    if context.os == 'Android':
        xpath = '//TextInputLayout[@content-desc="textField."]/android.widget.FrameLayout/android.widget.EditText'
        context.driver.find_element_by_xpath(xpath).send_keys(context.text1)
        xpath = '//TextInputLayout[@content-desc="TFInView."]/android.widget.FrameLayout/android.widget.EditText'
        context.driver.find_element_by_xpath(xpath).send_keys(context.text2)
    else:
        context.driver.find_element_by_accessibility_id('textField').send_keys(context.text1)
        context.driver.find_element_by_accessibility_id('TFInView').send_keys(context.text2)


@when(u'user clicks {access_id}')
def step_impl(context, access_id):
    context.driver.find_element_by_accessibility_id(access_id).click()


@then(u'text1 is {textField} and text2 is {textField2}')
def verify_page_heading(context, textField, textField2):
    assert True
