from selene import browser, by, be


def test_qa_registration():
    browser.config.base_url = 'https://app.qa.guru/automation-practice-form/'
    browser.open('/')

    browser.element('.MuiBox-root .css-1vpe9z').should(be.visible).click().element('MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-vubbuv')
    browser.element('#:r0:').type('Elina').press_enter()
    browser.element('#:r1:').type('Myagkova').press_enter()
    browser.element('#:r2:').type('kisterlina@gmail.com').press_enter()
    browser.element('#:r3:').type('+79996662211').press_enter()
    browser.element('MuiInputBase-input').click().element(
        by.text('Russian')).click()
    browser.element(':r4:').type('07071990').press_enter()


