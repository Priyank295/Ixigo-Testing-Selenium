# from Ixigo.base_test import BaseTest
# from Ixigo.flights_test import FlightsTest
from Ixigo.trains_test import TrainsTest


with TrainsTest() as test:
    test.home_screen()
    test.select_trains_mode()
    test.select_origin("Delhi")
    test.select_destination("Mumbai")
    test.select_date("24 September 2024")
    test.find()
    test.checking_all_sorting()
    # test.choose_trip('hotel')
    # test.open_login_tab()
    # test.enter_source("Bihar")
    # test.enter_destination("Delhi")
    # test.enter_date("30 August 2024")
    # test.select_adults("7")
    # test.add_hotels()
    # test.find()
    # test.sort_price()
    # test.sort_with_shortest()
    # test.checking_all_sorting()
    # test.changing_price_range("7000", "15000")
    # test.change_travellers("3")
    try:

        while True:  # Keep the script running indefinitely
            pass  # You can add test conditions here
    except KeyboardInterrupt:
        # Allow manual exit using Ctrl+C
        test.quit()

