from extensions import desktop_action
from utils.managers.manage_pages import ManagePages

def test_01_addition():
    desktop_action.click(ManagePages.cl.get_clear())
    desktop_action.click(ManagePages.cl.get_tow())
    desktop_action.click(ManagePages.cl.get_multi())
    desktop_action.click(ManagePages.cl.get_seven())
    desktop_action.click(ManagePages.cl.get_equels())



