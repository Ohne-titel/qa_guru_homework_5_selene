from selene import browser, by, be, have
import os.path

import tests


def should():
    pass


def test_qa_registration(browser_management):
    browser.open("/automation-practice-form")

    # WHEN
    browser.element("#firstName").should(be.blank).type("Elina")
    browser.element("#lastName").should(be.blank).type("Myagkova")
    browser.element("#userEmail").type("kisterlina@gmail.com")
    browser.element("#gender-radio-2").double_click()
    browser.element("#userNumber").type(9009998877)

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("July")
    ).click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1990")
    ).click()
    browser.element(".react-datepicker__day--007").click()

    browser.element("#subjectsInput").set_value("History").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element("#uploadPicture").set_value(
        os.path.abspath(
            os.path.join(os.path.dirname("tests"), "picture/Test vertical 640px.jpg")
        )
    )

    # THEN
    browser.element("#currentAddress").should(be.blank).type("India")
    browser.element("#react-select-3-input").type("Haryana").press_enter()
    browser.element("#react-select-4-input").type("Panipat").press_enter()
    browser.element("#submit").press_enter()

    browser.all("tbody tr:last-child").should(
        have.exact_texts(
            "Elina Myagkova",
            "kisterlina@gmail.com",
            "Female",
            "9009998877",
            "07 July,1990",
            "History",
            "Reading",
            # "Test vertical 640px.jpg",
            "India",
            "Haryana Panipat",
        )
    )
    browser.element("#closeLargeModal").press_enter()
