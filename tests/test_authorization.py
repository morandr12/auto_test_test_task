"""The module contains Test Suites Authorization"""

import pytest
import pytest_check
from loguru import logger
from pages.page_objects.main_page import MainPage
from pages.page_objects.user_profile_page import UserProfilePage
from data.users import user_tester


class TestSuiteAuthorization:

    user = user_tester

    def test_user_authorization(self, main_page: MainPage, user_profile_page: UserProfilePage):
        """Test user authorization"""
        logger.info("Start test_user_authorization")

        main_page.open()

        # chain of actions to log in
        main_page.header.head_bar.open_login_modal().input_login_data(
            email=self.user.email, password=self.user.password
        ).click_submit_button()

        assert (
            main_page.header.head_bar.is_user_link_present() is True
        ), "There is no link to the user's personal account"

        pytest_check.equal(
            main_page.header.head_bar.get_text_from_user_link(),
            f"{self.user.name} {self.user.surname}",
            msg="Users name and surename from login link are not equal expected user name and surename",
        )

        main_page.header.head_bar.go_to_user_profile_page()

        pytest_check.equal(
            user_profile_page.user_name,
            self.user.name,
            msg="Users name is not equal expected user name",
        )
        pytest_check.equal(
            user_profile_page.user_surename,
            self.user.surname,
            msg="Users surename is not equal expected user surename",
        )
        pytest_check.equal(
            user_profile_page.user_phone,
            self.user.phone,
            msg="Users phone is not equal expected user phone",
        )
        pytest_check.equal(
            user_profile_page.user_email,
            self.user.email,
            msg="Users email is not equal expected user email",
        )

    class TestSuiteAuthorizationNegative:

        empty_password = {"email": user_tester.email, "password": ""}
        empty_email = {"email": "", "password": user_tester.password}
        incorrect_password = {"email": user_tester.email, "password": user_tester.password[:-1]}
        incorrect_email = {
            "email": user_tester.email.replace(".com", ".ru"),
            "password": user_tester.password,
        }

        @pytest.mark.negative
        @pytest.mark.parametrize(
            "user_data", [empty_password, empty_email, incorrect_password, incorrect_email]
        )
        def test_user_authorization_negative(self, main_page: MainPage, user_data):
            """Test user authorization negative"""
            logger.info("Start test_user_authorization_negative")

            main_page.open()

            # chain of actions to log in
            login_modal = (
                main_page.header.head_bar.open_login_modal()
                .input_login_data(email=user_data.get("email"), password=user_data.get("password"))
                .click_submit_button()
            )

            pytest_check.is_(
                login_modal.is_there_invalid_feedback(),
                True,
                msg="There is no invalid login feedback",
            )

            assert (
                main_page.header.head_bar.is_user_link_present() is False
            ), "There is link to the user's personal account"
