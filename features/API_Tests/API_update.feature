@web
Feature: Computer can be updated, including validation

    Background:Navigate to edit Computer page
        Given A user has created a computer with known details for updating via the API


#    Scenario Outline: User can Edit computer with valid data
#        Given computer <Computer_name> does not exist for API testing
#        When a user updates record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"
#        Then the response status should be 200
#        Then the computer is updated on the table with the correct information
#        And delete computer cleanup edit
#
#        Examples:
#        |Computer_name   |Introduced_Date|Discontinued_Date|Company           |
#        |BBRC_edit_Test_1|null           |null             |null              |
#        |BBRC_edit_Test_2|2008-02-29     |null             |null              |
#        |BBRC_edit_Test_3|2020-04-30     |2002-04-30       |null              |
#        |BBRC_edit_Test_4|2004-7-1       |2020-02-29       |IBM               |
#        |BBRC_edit_Test_5|null           |2020-02-29       |RCA               |
#        |BBRC_edit_Test_6|null           |null             |Thinking Machines |
#        |BBRC_edit_Test_7|1997-09-05     |null             |IBM               |
#        |BBRC_edit_Test_8|null           |1986-04-07       |null              |
#


    Scenario Outline: User cannot edit a computer with invalid data
        Given computer <Computer_name> does not exist for API testing
        When a user updates record with name "<Computer_name>", intro_date "<Introduced_Date>", discon_date "<Discontinued_Date>" and company "<Company>"
        Then the response status should be 400
        And the computer will be not have been updated in the UI

        Examples:
        |Computer_name                  |Introduced_Date|Discontinued_Date|Company        |
        |null                           |2008-01-01     |2008-01-01       |IBM            |
        |BBRC_edit_invalid_intro_date1  |2008/01/01     |null             |null           |
        |BBRC_edit_invalid_intro_date2  |29-02-2008     |null             |null           |
        |BBRC_edit_invalid_intro_date3  |29/02/2008     |null             |null           |
        |BBRC_edit_invalid_intro_date4  |test           |null             |null           |
        |BBRC_edit_invalid_intro_date5  |2007-02-29     |null             |null           |
        |BBRC_edit_invalid_discon_date1 |null           |2008/01/01       |null           |
        |BBRC_edit_invalid_discon_date2 |null           |29-02-2008       |null           |
        |BBRC_edit_invalid_discon_date3 |null           |29/02/2008       |null           |
        |BBRC_edit_invalid_discon_date4 |null           |test             |null           |
        |BBRC_edit_invalid_discon_date5 |null           |2007-02-29       |null           |
        |null                           |2008/01/01     |29-02-2008       |null           |
        |BBRC_edit_invalid_company      |2008-02-29     |2020-02-29       |invalid company|




