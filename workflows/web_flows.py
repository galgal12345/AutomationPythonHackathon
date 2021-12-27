from extensions import ui_actions
from utils.manage_pages import ManagePages


def login_flow(user_name, password):
    ui_actions.set_text(ManagePages.lp.locator_input_user_name, user_name)
    ui_actions.set_text(ManagePages.lp.locator_input_password, password)
    ui_actions.click(ManagePages.lp.locator_button_sign_in)


def get_user_name_txt():
    return ManagePages.mp.txt_user_name().text


def register_flow(first_name, last_name, user_name, password):
    e = ManagePages.lp.locator_link_sign_up
    ui_actions.click(e)
    ui_actions.click(e)
    ui_actions.set_text(ManagePages.su.locator_input_first_name, first_name)
    ui_actions.set_text(ManagePages.su.locator_input_last_name, last_name)
    ui_actions.set_text(ManagePages.su.locator_input_user_name, user_name)
    ui_actions.set_text(ManagePages.su.locator_input_password, password)
    ui_actions.set_text(ManagePages.su.locator_input_confirm_password, password)
    ui_actions.click(ManagePages.su.locator_button_sign_up)
